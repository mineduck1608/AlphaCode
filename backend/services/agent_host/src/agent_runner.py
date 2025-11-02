# Agent host (ADK-like orchestration) that talks to Gemini and MCP servers via STDIO
import os
import time
import json
from mcp_process import MCPProcess
import google.generativeai as genai

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
MODEL = os.getenv("LLM_MODEL","gemini-1.5-pro")

if GENAI_API_KEY:
    genai.configure(api_key=GENAI_API_KEY)


def call_gemini(prompt: str, schema: dict = None) -> str:
    # simple text generation; you can extend to structured outputs
    model = genai.Predictions() if hasattr(genai, 'Predictions') else genai
    resp = genai.generate_content(model=MODEL, prompt=prompt)
    # adapt to real sdk response shape
    text = getattr(resp, 'text', None) or (resp.get('candidates')[0].get('content') if isinstance(resp, dict) else str(resp))
    return text


def main():
    # start MCP servers (paths assume running from repo root)
    vec_cmd = ["python", "services/mcp_vector/src/server.py"]
    an_cmd = ["python", "services/mcp_analyzer/src/server.py"]

    vec_proc = MCPProcess(vec_cmd)
    an_proc = MCPProcess(an_cmd)

    # read initial caps
    print("Vector server init:", vec_proc.recv(timeout=2))
    print("Analyzer server init:", an_proc.recv(timeout=2))

    # Example flow: user gives SRS text
    srs_text = "As a user, I want the system to export reports soon so that managers can review them."

    # ingest into vector store
    vec_proc.send({"id": "1", "method": "ingest", "params": {"ids": ["doc1-chunk1"], "texts": [srs_text], "metadatas": [{"source":"upload"}]}})
    print("Ingest resp:", vec_proc.recv(timeout=2))

    # semantic search
    vec_proc.send({"id": "2", "method": "search", "params": {"query": "export reports manager", "top_k": 3}})
    search_resp = vec_proc.recv(timeout=4)
    print("Search resp:", search_resp)

    # call analyzer with chunk(s)
    chunks = [srs_text]
    an_proc.send({"id": "3", "method": "analyze_requirement", "params": {"chunks": chunks}})
    an_resp = an_proc.recv(timeout=4)
    print("Analyze resp:", an_resp)

    # ask Gemini to generate a user-facing explanation / improvement suggestions
    prompt = "Given the analysis: %s; Suggest improvements in JSON format." % (json.dumps(an_resp))
    gem_out = call_gemini(prompt)
    print("Gemini suggestion:\n", gem_out)

    # cleanup
    vec_proc.terminate()
    an_proc.terminate()


if __name__ == '__main__':
    main()
