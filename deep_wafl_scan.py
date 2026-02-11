import pickle
import re

print("Deep scanning local index for WAFL command context...")

try:
    with open('temp_2', 'rb') as f:
        docs = pickle.load(f)

    # Search for any line containing "WAFL" that looks like a command or prompt
    for doc in docs:
        content = str(doc).lower()
        if "wafl" in content:
            # Split into lines and look for commands
            lines = str(doc.get('content', '')).split('\n')
            for line in lines:
                if "wafl" in line.lower() and (">" in line or "#" in line or "$" in line or "type" in line or "command" in line.lower()):
                    print(f"Match in {doc.get('name')}: {line.strip()[:300]}")
                    
    # Also search for "hwdiag" usage to see if WAFL is a parameter
    print("\nChecking hwdiag parameters for WAFL...")
    for doc in docs:
        content = str(doc).lower()
        if "hwdiag" in content and "wafl" in content:
            print(f"Hwdiag match in {doc.get('name')}: {doc.get('content', '')[:500]}")

except Exception as e:
    print(e)
