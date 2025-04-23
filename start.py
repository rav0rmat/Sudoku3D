## `start.py`
python
import os
import sys
NOTEBOOK = "Sudoku_3D_UI.ipynb"
PORT = os.environ.get("PORT", "8080")
print("✅ Execut notebookul în fundal...")
# os.system(f"jupyter nbconvert --execute --inplace {NOTEBOOK}")
print("🟢 Lansăm Voilà pe 0.0.0.0…")
os.execvp("voila", [
    "voila", NOTEBOOK,
    "--port", PORT,
    "--no-browser",
    "--Voila.ip=0.0.0.0",
    "--strip_sources=True",
    "--theme=dark"
])

