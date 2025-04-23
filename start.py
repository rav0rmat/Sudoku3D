import os

print("✅ Execut notebookul în fundal...")
os.system("jupyter nbconvert --execute --inplace Sudoku_3D_Voila_Final.ipynb")

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
