import re
from pathlib import Path
from researchclaw.templates.compiler import compile_latex

out_dir = Path("artifacts/rc-20260330-061112-a2ffee/deliverables")
tex_path = out_dir / "paper.tex"

tex = tex_path.read_text(encoding="utf-8")

tex = re.sub(r"\\usepackage\{adjustbox\}", "", tex)
tex = re.sub(r"\\begin\{adjustbox\}\{.*?\}", "", tex)
tex = tex.replace("\\end{adjustbox}", "")
tex = re.sub(r"\\usepackage\{amsfonts\}", "", tex)
tex = re.sub(r"\\usepackage\{amsmath\}", "", tex)

tex_path.write_text(tex, encoding="utf-8")

print("Compiling locally...")
result = compile_latex(tex_path, max_attempts=2)
if result.success:
    print("Local compilation SUCCESS!")
else:
    for e in result.errors:
        print(e)
