import pickle
import sys

try:
    with open('temp_2', 'rb') as f:
        data = pickle.load(f)
    print("TYPE:", type(data))
    print("LEN:", len(data))
    if len(data) > 0:
        print("FIRST_ELEM_TYPE:", type(data[0]))
        # print("FIRST_ELEM_KEYS:", data[0].keys() if isinstance(data[0], dict) else "N/A")
except Exception as e:
    print(f"ERROR: {e}")
