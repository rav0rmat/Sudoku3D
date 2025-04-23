import os

print("✅ Execut notebookul în fundal...")
os.system("jupyter nbconvert --execute --inplace Sudoku_3D_Voila_Final.ipynb")

print("🟢 Lansăm Voilà...")
os.system("voila Sudoku_3D_Voila_Final.ipynb --port=$PORT --no-browser --theme=dark --strip_sources=True")