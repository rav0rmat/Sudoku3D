## `auto_repair_pipeline.sh`
```bash
#!/usr/bin/env bash
set -e
# 1 pull
git pull
# 2 test
python3 test_notebook.py && exit 0 || true
# 3 AI repair
python3 send_to_gpt_env.py
# 4 replace & push
mv Sudoku3D_Fixed.ipynb Sudoku_3D_UI.ipynb
git add Sudoku_3D_UI.ipynb
git commit -m "Auto-fix by GPT"
git push
```
