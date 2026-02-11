import pickle
import re

print("Starting Offline RAG search for PCIe status commands...")

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    keywords = ["pcie", "status", "test", "command", "check", "lsdev", "lspci"]
    matches = []

    for doc in docs:
        content = str(doc).lower()
        # Find docs that mention pcie and status or command
        if "pcie" in content and ("status" in content or "command" in content or "check" in content):
            matches.append(doc)
            if len(matches) > 5: break

    if matches:
        for i, m in enumerate(matches):
            print(f"\n--- Result {i+1} ---")
            print(str(m)[:2000])
    else:
        print("No matches found for PCIe status in local index.")

except Exception as e:
    print(f"Error during search: {e}")
