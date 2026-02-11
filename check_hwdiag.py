import pickle

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    # Search for hwdiag pcie
    results = []
    for doc in docs:
        content = str(doc).lower()
        if "hwdiag" in content and "pcie" in content:
            results.append(doc)
            if len(results) > 5: break

    for i, r in enumerate(results):
        print(f"\n--- HWDIAG MATCH {i} ---")
        print(str(r)[:1000])

except Exception as e:
    print(e)
