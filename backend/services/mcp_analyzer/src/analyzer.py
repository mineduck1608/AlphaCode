# Simple rule-based analyzer helpers. Extend with stronger heuristics or LLM-assisted checks.
from typing import List, Dict, Any

def detect_ambiguous_terms(text: str) -> List[Dict[str, Any]]:
    issues = []
    # naive example: flag words like "soon", "appropriate", "fast" as ambiguous
    ambiguous_keywords = ["soon", "appropriate", "fast", "quickly", "as needed", "user friendly"]
    for kw in ambiguous_keywords:
        if kw in text.lower():
            issues.append({
                "type": "ambiguity",
                "keyword": kw,
                "description": f"Found ambiguous term '{kw}'. Consider specifying measurable criteria."
            })
    return issues


def detect_missing_acceptance_criteria(stories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    issues = []
    for s in stories:
        if not s.get("acceptance_criteria"):
            issues.append({
                "type": "missing",
                "description": f"User story '{s.get('title','(no title)')}' has no acceptance criteria."
            })
    return issues


def cross_check_conflicts(stories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    issues = []
    # naive pairwise check: look for direct contradictions in short forms
    for i in range(len(stories)):
        for j in range(i+1, len(stories)):
            a = stories[i].get('description','')
            b = stories[j].get('description','')
            if "only admin" in a.lower() and "everyone" in b.lower():
                issues.append({
                    "type": "conflict",
                    "description": f"Possible conflict between stories {i} and {j}: one restricts to admins, the other allows everyone."
                })
    return issues


def analyze_text_chunks(chunks: List[str], options: Dict = None) -> Dict:
    options = options or {}
    all_text = "\n\n".join(chunks)
    issues = []
    issues.extend(detect_ambiguous_terms(all_text))
    # placeholder: we expect caller to pass structured stories if available
    return {"summary": all_text[:400], "issues": issues}
# orchestrate rules