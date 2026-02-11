import pickle
import re

print("Searching offline RAG for CPLD register power good definitions...")

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    keywords = ["cpld", "register", "power good", "pwr_gd", "pwrgd"]
    matches = []

    for doc in docs:
        content = str(doc).lower()
        # Look for docs that contain CPLD and Power Good and Register
        if "cpld" in content and ("power good" in content or "pwr_gd" in content or "pwrgd" in content):
            if "register" in content or "offset" in content:
                matches.append(doc)
                if len(matches) > 3: break

    if matches:
        for i, m in enumerate(matches):
            print(f"\n--- Result {i+1} (Source: {m.get('name')}) ---")
            print(str(m.get('content'))[:2000])
    else:
        print("No specific match found for CPLD register power good.")

except Exception as e:
    print(f"Error: {e}")
