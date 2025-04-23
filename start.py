# start.py
import os

# Fișierul notebook de rulat
NOTEBOOK = "Sudoku_3D_Voila_Final.ipynb"
# Preia portul din mediu sau folosește 8080 implicit
PORT = os.environ.get("PORT", "8080")

# Conversia și execuția notebook-ului
print("✅ Execut notebookul în fundal...")
os.system(f"jupyter nbconvert --execute --inplace {NOTEBOOK}")

# Lansăm Voilà pe toate interfețele la portul corect
print("🟢 Lansăm Voilà pe 0.0.0.0…")
os.execvp("voila", [
    "voila",
    NOTEBOOK,
    "--port", PORT,
    "--ip", "0.0.0.0",
    "--no-browser",
    "--theme", "dark",
    "--strip_sources", "True"
])

