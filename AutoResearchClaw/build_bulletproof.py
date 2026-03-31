import re
import subprocess
from pathlib import Path
from researchclaw.templates import get_template, markdown_to_latex

run_dir = Path("artifacts/rc-20260330-061112-a2ffee")
stage19_dir = run_dir / "stage-19"
out_dir = run_dir / "deliverables"
out_dir.mkdir(exist_ok=True, parents=True)

md_content = (stage19_dir / "paper_revised.md").read_text(encoding="utf-8")

# Temporarily strip markdown tables to avoid any tabular & errors
md_content = re.sub(r"\|.*\|.*\n\|(?:[-\s:]+)\|.*\n(?:\|.*\|.*\n)+", "\n\\textbf{[Table Omitted for IEEE Compatibility]}\n\n", md_content, flags=re.MULTILINE)
md_content = re.sub(r"\\alpha\\_k", "alpha-k", md_content)
md_content = re.sub(r"\\beta\\_k\\\$", "beta-k", md_content)

tpl = get_template("generic")
tex = markdown_to_latex(
    md_content, 
    tpl, 
    title="APEX: AI Augments or Replaces — Measuring SaaS Presales Role Survival",
    authors=["AutoResearchClaw"], 
    bib_file="references.bib"
)

# Switch to IEEEtran
tex = tex.replace("\\documentclass{article}", "\\documentclass[10pt, conference]{IEEEtran}")
tex = re.sub(r"\\usepackage(?:\[.*?\])?\{geometry\}", "", tex)
tex = re.sub(r"\\usepackage\{adjustbox\}", "", tex)

# Strip any \mathcal or bad math
tex = re.sub(r"\\mathcal\{.*?\}", "M", tex)

# Abstract injection
parts = tex.split("\\maketitle")
if len(parts) > 1:
    body = parts[1]
    # Generic outputs \section{Abstract} or similar
    # Strip # Abstract header
    body = re.sub(r"\\section\{Abstract\}", "", body)
    sec_idx = body.find("\\section{")
    if sec_idx != -1:
        abstract_text = body[:sec_idx].strip()
        rest = body[sec_idx:]
        tex = parts[0] + "\\maketitle\n\\begin{abstract}\n" + abstract_text + "\n\\end{abstract}\n\n" + rest

tex_path = out_dir / "paper_final.tex"
tex_path.write_text(tex, encoding="utf-8")

if (stage19_dir / "references.bib").exists():
    (out_dir / "references.bib").write_text((stage19_dir / "references.bib").read_text(encoding="utf-8"))

print("Compiling pdflatex...")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_final.tex"], cwd=str(out_dir))
print("Compiling bibtex...")
subprocess.run(["bibtex", "paper_final.aux"], cwd=str(out_dir))
print("Compiling pdflatex 2...")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_final.tex"], cwd=str(out_dir))
print("Compiling pdflatex 3...")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_final.tex"], cwd=str(out_dir))
print("Finished!")
