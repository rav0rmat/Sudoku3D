## `test_notebook.py`
```python
import subprocess, sys
NOTEBOOK = "Sudoku_3D_UI.ipynb"
ERROR_LOG = "error.log"
print(f"🧪 Test {NOTEBOOK}")
res = subprocess.run(["jupyter","nbconvert","--execute","--inplace",NOTEBOOK], stderr=subprocess.PIPE)
if res.returncode==0:
    print("✅ OK")
    sys.exit(0)
else:
    print("❌ Eroare")
    open(ERROR_LOG,"wb").write(res.stderr)
    sys.exit(1)
```
