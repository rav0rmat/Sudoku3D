import os

print("✅ Execut notebookul în fundal...")
os.system("jupyter nbconvert --execute --inplace Sudoku_3D_Voila_Final.ipynb")

print("🟢 Lansăm Voilà...")
os.system(f"voila Sudoku_3D_Voila_Final.ipynb --port={os.environ['PORT']} --no-browser --theme=dark --strip_sources=True")
