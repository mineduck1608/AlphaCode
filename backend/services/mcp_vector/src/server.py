# expose tools: ingest, search
import sys
import json
import traceback
from vector import VectorStore

# simple global vector store instance
VECTOR = VectorStore(persist_directory=None)


def send(obj):
	sys.stdout.write(json.dumps(obj) + "\n")
	sys.stdout.flush()


def handle(msg):
	try:
		method = msg.get("method")
		params = msg.get("params", {})
		if method == "ingest":
			ids = params["ids"]
			texts = params["texts"]
			metadatas = params.get("metadatas", [None]*len(ids))
			VECTOR.upsert(ids, texts, metadatas)
			return {"ok": True}
		elif method == "search":
			q = params["query"]
			top_k = params.get("top_k", 5)
			res = VECTOR.query(q, n_results=top_k)
			return {"ok": True, "result": res}
		else:
			return {"error": f"unknown method {method}"}
	except Exception as e:
		return {"error": str(e), "trace": traceback.format_exc()}


def run():
	send({"capabilities": ["ingest", "search"], "name": "mcp_vector"})
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
# expose tools: ingest, search