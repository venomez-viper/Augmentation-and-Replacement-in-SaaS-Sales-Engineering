import re
from pathlib import Path
from researchpipeline.templates.compiler import compile_latex

out_dir = Path("artifacts/rc-20260330-061112-a2ffee/deliverables")
tex_path = out_dir / "paper.tex"
ieee_path = out_dir / "paper_ieee.tex"

tex = tex_path.read_text(encoding="utf-8")

ieee_path.write_text(tex, encoding="utf-8")

print("Compiling locally...")
result = compile_latex(ieee_path, max_attempts=2)
if result.success:
    print("Local compilation SUCCESS!")
else:
    for e in result.errors:
        print(e)
