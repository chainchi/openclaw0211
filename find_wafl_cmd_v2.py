import pickle
import re

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    # Looking for command patterns
    cmd_patterns = [
        r"wafl\s+status",
        r"check\s+wafl",
        r"show\s+wafl",
        r"diag\s+wafl",
        r"hwdiag\s+wafl",
        r"spsh.*wafl"
    ]

    results = []
    for doc in docs:
        content = str(doc).lower()
        if "wafl" in content:
            for p in cmd_patterns:
                if re.search(p, content):
                    results.append(doc)
                    break
            if len(results) > 10: break

    if results:
        for i, r in enumerate(results):
            print(f"\n--- MATCH {i} ---")
            print(f"File: {r.get('name', 'N/A')}")
            # Print around where WAFL is mentioned
            content = str(r.get('content', ''))
            wafl_idx = content.lower().find("wafl")
            start = max(0, wafl_idx - 200)
            end = min(len(content), wafl_idx + 500)
            print(content[start:end])
    else:
        # Fallback: just search for any command-like line with WAFL
        print("No direct command pattern found, searching for general WAFL lines...")
        for doc in docs:
            content = str(doc).lower()
            if "wafl" in content:
                lines = content.split('\n')
                for line in lines:
                    if "wafl" in line and (">" in line or "#" in line or "$" in line or "type" in line):
                        print(f"Potential: {line[:200]}")

except Exception as e:
    print(e)
