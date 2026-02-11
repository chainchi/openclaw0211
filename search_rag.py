import pickle
import re

with open('temp_2', 'rb') as f:
    docs = pickle.load(f)

search_terms = [
    "Find E6 ROT IP",
    "HWDiag System Fabric Test",
    "Poll BKC firmware update",
    "Check ILOM or AMI BMC status",
    "Login E6 ILOM or AMI BMC",
    "Find ILOM or AMI BMC IP"
]

results = {}

for term in search_terms:
    matches = []
    for doc in docs:
        if term.lower() in str(doc).lower():
            # Extract some context
            matches.append(str(doc)[:1000])
            if len(matches) > 2: break
    results[term] = matches

for term, matches in results.items():
    print(f"--- TERM: {term} ---")
    if matches:
        print(matches[0])
    else:
        print("No matches found.")
