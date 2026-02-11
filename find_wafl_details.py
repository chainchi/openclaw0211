import pickle

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    results = []
    # Search for "WAFL" and look for lines that look like commands
    for doc in docs:
        content = str(doc).lower()
        if "wafl" in content:
            # Print a bit more context to find the actual command
            results.append(doc)
            if len(results) > 10: break

    for i, r in enumerate(results):
        print(f"\n--- WAFL Context {i} ---")
        # Print the name of the file and the content
        print(f"File: {r.get('name', 'N/A')}")
        print(str(r.get('content', ''))[:3000])

except Exception as e:
    print(e)
