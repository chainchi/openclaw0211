import pickle

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    # Search for commands like hwdiag, pcie_status, or similar
    results = []
    for doc in docs:
        content = str(doc).lower()
        if "pcie" in content and ("command" in content or "diag" in content):
            if "status" in content or "check" in content:
                results.append(doc)
                if len(results) > 10: break

    for i, r in enumerate(results):
        print(f"\n--- MATCH {i} ---")
        print(str(r)[:1000])

except Exception as e:
    print(e)
