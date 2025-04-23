## `send_to_gpt_env.py`
python
import openai, os
NOTEBOOK="Sudoku_3D_UI.ipynb"; ERROR_LOG="error.log"; OUTPUT="Sudoku3D_Fixed.ipynb"
openai.api_key=os.environ.get("OPENAI_API_KEY")
if not openai.api_key: raise RuntimeError("Missing OPENAI_API_KEY")
code=open(NOTEBOOK).read(); err=open(ERROR_LOG).read()
prompt=f"""Ai acest notebook cu eroare. Corectează!\nNotebook:\n{code}\nEroare:\n{err}"""
resp=openai.ChatCompletion.create(model="gpt-4", messages=[{"role":"user","content":prompt}], temperature=0)
fixed=resp.choices[0].message.content
open(OUTPUT,"w").write(fixed)
print(f"✅ GPT a returnat {OUTPUT}")

