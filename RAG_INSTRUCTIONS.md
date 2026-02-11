# FOX RAG Protocol

Use this protocol when the user asks a question that might require internal knowledge (FOX RAG).

**Target Node:** `5829e449628736a48a16c6983f76ea1f0da3bdf966137e742d2fe58347a028ad` (Lawrence-PC)
**Target URL:** `http://127.0.0.1:5000/` (or search for tab "FOX RAG System")
**Profile:** `openclaw`

## Query Steps (Offline First Priority)

1.  **PRIMARY: Local Search:** 
    - Always start by searching local index files: `temp_1`, `temp_2`, `temp_3` in the workspace.
    - Use a Python script to search the `.pkl` (list of dicts) data for user keywords.
    - Extract relevant SOP content and report to the user immediately.

2.  **SECONDARY: Online RAG (Fallback):**
    - If local search yields no results AND Lawrence-PC is connected, then try:
    - Target Node: `Lawrence-PC`
    - Target URL: `http://127.0.0.1:5000/`
