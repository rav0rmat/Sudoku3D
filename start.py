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
  "Sudoku_3D_Voila_Final.ipynb",
  "--port", PORT,
  "--no-browser",
  "--Voila.ip=0.0.0.0",
  "--strip_sources=True",
  "--theme=dark"
])


