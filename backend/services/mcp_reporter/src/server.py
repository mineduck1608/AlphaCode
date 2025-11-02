# STDIO MCP server: Reporter Agent (generate reports / summaries)
import sys
import json
import traceback


def send(obj):
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


def handle(msg):
    try:
        method = msg.get("method")
        params = msg.get("params", {})
        if method == "generate_report":
            requirements = params.get("requirements", [])
            # naive report: summarize titles and priorities
            report = {
                "count": len(requirements),
                "items": [{"id": r.get("id"), "title": r.get("title"), "priority": r.get("priority")} for r in requirements]
            }
            return {"ok": True, "report": report}
        elif method == "diagram":
            # return a simple dot-like adjacency placeholder
            nodes = [r.get("id") for r in params.get("requirements", [])]
            diagram = {"type": "nodes", "nodes": nodes}
            return {"ok": True, "diagram": diagram}
        elif method == "markdown_table":
            # return a markdown table summarizing requirements
            requirements = params.get("requirements", [])
            lines = ["| id | title | priority |", "|---|---|---|"]
            for r in requirements:
                lines.append(f"| {r.get('id')} | {r.get('title')} | {r.get('priority', '')} |")
            return {"ok": True, "markdown": "\n".join(lines)}
        elif method == "mermaid_diagram":
            # create a very simple mermaid graph showing dependencies if provided
            requirements = params.get("requirements", [])
            edges = params.get("edges", [])  # list of (from,to)
            mermaid = ["graph TD"]
            for r in requirements:
                mermaid.append(f"    {r.get('id')}[\"{r.get('title')}\"]")
            for e in edges:
                frm = e[0]
                to = e[1]
                mermaid.append(f"    {frm} --> {to}")
            return {"ok": True, "mermaid": "\n".join(mermaid)}
        elif method == "build_final_report":
            # If LLM is available and prompts exist, use the prompt to synthesize final report
            requirements = params.get("core_requirements", [])
            analyzer_output = params.get("analyzer_output", {})
            project_id = params.get("project_id", "default")
            try:
                # read promt from prompts folder
                from pathlib import Path
                import yaml
                from jinja2 import Template
                p = Path(__file__).resolve().parents[4] / "prompts" / "reporter.yml"
                prompt_text = None
                if p.exists():
                    doc = yaml.safe_load(p.read_text())
                    node = doc.get("prompts", {}).get("build_final_report")
                    if node:
                        tpl = Template(node.get("template", ""))
                        prompt_text = tpl.render(project_id=project_id, core_requirements=requirements, analyzer_output=analyzer_output)
            except Exception:
                prompt_text = None

            if prompt_text and 'GENAI_API_KEY' in __import__('os').environ:
                try:
                    import google.generativeai as genai
                    genai.configure(api_key=__import__('os').environ.get('GENAI_API_KEY'))
                    resp = genai.chat.create(model=__import__('os').environ.get('LLM_MODEL', 'chat-bison-001'), messages=[{"role": "user", "content": prompt_text}], max_output_tokens=1024)
                    content = resp.last['candidates'][0]['content']
                    # best-effort: return LLM content as single artifact
                    return {"ok": True, "report": {"llm_content": content}}
                except Exception:
                    pass

            # fallback: construct simple artifacts
            md_lines = ["# Executive Summary", "\nTop requirements:"]
            md_lines.append("\n| id | title | priority |")
            md_lines.append("|---|---|---|")
            for r in (requirements[:5] if isinstance(requirements, list) else []):
                md_lines.append(f"| {r.get('id')} | {r.get('title')} | {r.get('priority','')} |")
            csv_lines = ["req_id,title,priority,priority_score,estimated_effort,confidence,recommended_action"]
            for r in requirements:
                csv_lines.append(f"{r.get('id')},{r.get('title')},{r.get('priority','')},{r.get('score','')},{r.get('estimated_effort','')},{r.get('confidence','')},{r.get('recommended_action','')}")
            mermaid = ["graph TD"]
            for r in requirements:
                mermaid.append(f"    {r.get('id')}[\"{r.get('title')}\"]")
            return {"ok": True, "final_report_markdown": "\n".join(md_lines), "final_report_csv": "\n".join(csv_lines), "final_report_mermaid": "\n".join(mermaid)}
        else:
            return {"error": f"unknown method {method}"}
    except Exception as e:
        return {"error": str(e), "trace": traceback.format_exc()}


def run():
    send({"capabilities": ["generate_report", "diagram"], "name": "mcp_reporter"})
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
        except Exception:
            send({"error": "invalid json"})
            continue
        resp = handle(msg)
        send({"id": msg.get("id"), "response": resp})


if __name__ == "__main__":
    run()
