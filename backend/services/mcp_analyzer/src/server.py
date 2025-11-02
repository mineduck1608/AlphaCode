# STDIO MCP server for requirement analysis
import sys
import json
import traceback
from analyzer import analyze_text_chunks, detect_missing_acceptance_criteria, cross_check_conflicts


def send(obj):
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


def handle(msg):
    try:
        method = msg.get("method")
        params = msg.get("params", {})
        if method == "analyze_requirement":
            chunks = params.get("chunks") or []
            options = params.get("options", {})
            res = analyze_text_chunks(chunks, options=options)
            return {"ok": True, "result": res}
        elif method == "analyze_stories":
            stories = params.get("stories", [])
            issues = []
            issues.extend(detect_missing_acceptance_criteria(stories))
            issues.extend(cross_check_conflicts(stories))
            return {"ok": True, "result": {"issues": issues}}
        else:
            return {"error": f"unknown method {method}"}
    except Exception as e:
        return {"error": str(e), "trace": traceback.format_exc()}


def run():
    send({"capabilities": ["analyze_requirement", "analyze_stories"], "name": "mcp_analyzer"})
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
# expose tool: analyze_requirement