import pickle

print("Searching local RAG index for 'WAFL'...")

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    matches = []
    for doc in docs:
        content = str(doc).lower()
        if "wafl" in content:
            matches.append(doc)
            if len(matches) > 5: break

    if matches:
        for i, m in enumerate(matches):
            print(f"\n--- Result {i+1} ---")
            print(str(m)[:1500])
    else:
        print("No WAFL related documentation found in local index.")

except Exception as e:
    print(f"Error: {e}")
