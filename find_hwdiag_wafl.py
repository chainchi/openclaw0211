import pickle

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    # Looking for the specific command format
    results = []
    for doc in docs:
        content = str(doc).lower()
        if "wafl" in content:
            # Look for lines that contain hwdiag and wafl
            lines = str(doc.get('content', '')).split('\n')
            for line in lines:
                if "hwdiag" in line.lower() and "wafl" in line.lower():
                    results.append(f"File: {doc.get('name')} | Line: {line.strip()}")
            if len(results) > 10: break

    if results:
        for r in results:
            print(r)
    else:
        # If not found in lines, print snippets of files mentioning both
        print("No direct line match, checking snippets...")
        for doc in docs:
            content = str(doc).lower()
            if "hwdiag" in content and "wafl" in content:
                print(f"Match in {doc.get('name')}:")
                print(str(doc.get('content'))[:1000])

except Exception as e:
    print(e)
