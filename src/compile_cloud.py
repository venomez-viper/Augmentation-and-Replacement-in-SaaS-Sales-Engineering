import tarfile
import requests
import re
from pathlib import Path

run_dir = Path("artifacts/rc-20260330-061112-a2ffee")
out_dir = run_dir / "deliverables"
tex_path = out_dir / "paper.tex"

tex = tex_path.read_text(encoding="utf-8")

# Strip all figures completely
tex = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", "", tex, flags=re.DOTALL)
tex = re.sub(r"\\includegraphics\[.*?\]\{.*?\}", "", tex)

def math_repl(m):
    return m.group(1).replace("\\", "").replace("_", "-").replace("{", "").replace("}", "")
tex = re.sub(r"(?<!\\)\$([^\$]+)(?<!\\)\$", math_repl, tex)

tex_path.write_text(tex, encoding="utf-8")

print("Creating project.tar.gz...")
with tarfile.open("project.tar.gz", "w:gz") as tar:
    tar.add(str(out_dir / "paper.tex"), arcname="paper.tex")
    if (out_dir / "references.bib").exists():
        tar.add(str(out_dir / "references.bib"), arcname="references.bib")

url = "https://latexonline.cc/data?target=paper.tex"
print(f"Sending to {url}...")
with open("project.tar.gz", "rb") as f:
    response = requests.post(url, files={"file": f})

if response.status_code == 200:
    (out_dir / "paper_ieee.pdf").write_bytes(response.content)
    print("PDF successfully downloaded!")
else:
    print("Error compiling online:", response.status_code)
    print(response.text[-2000:])
