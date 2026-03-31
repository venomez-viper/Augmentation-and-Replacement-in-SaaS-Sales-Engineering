import sys
import re
import subprocess
from pathlib import Path
from researchclaw.templates import get_template, markdown_to_latex
from researchclaw.experiment.visualize import generate_all_charts
from researchclaw.templates.compiler import remove_missing_figures

run_dir = Path("artifacts/rc-20260330-061112-a2ffee")
stage19_dir = run_dir / "stage-19"
out_dir = run_dir / "deliverables"
chart_dir = out_dir / "charts"
chart_dir.mkdir(exist_ok=True, parents=True)

print("Generating charts...")
try:
    generate_all_charts(run_dir, chart_dir, metric_key="rsi", metric_direction="maximize")
    print("Charts generated!")
except Exception as e:
    print("Chart generation failed:", e)

md_content = (stage19_dir / "paper_revised.md").read_text(encoding="utf-8")

md_content = md_content.replace(" —", ":")
md_content = md_content.replace("—", "-")
md_content = md_content.replace("APEX: AI Augments or Replaces:", "APEX: AI Augments or Replaces:")

md_content = re.sub(r"\|.*\|.*\n\|(?:[-\s:]+)\|.*\n(?:\|.*\|.*\n)+", "\n\\textbf{[Table Omitted]}\n\n", md_content, flags=re.MULTILINE)
md_content = re.sub(r"\\alpha\\_k", "alpha-k", md_content)
md_content = re.sub(r"\\beta\\_k\\\$", "beta-k", md_content)

tpl = get_template("generic")
tex = markdown_to_latex(
    md_content, 
    tpl, 
    title="APEX: AI Augments or Replaces: Measuring SaaS Presales Role Survival",
    authors=["Akash Anipakalu Giridhar"], 
    bib_file="references.bib"
)

tex = tex.replace("\\documentclass{article}", "\\documentclass[10pt, conference]{IEEEtran}")
tex = re.sub(r"\\usepackage(?:\[.*?\])?\{geometry\}", "", tex)
tex = re.sub(r"\\usepackage\{adjustbox\}", "", tex)
tex = re.sub(r"\\mathcal\{.*?\}", "M", tex)

tex = re.sub(r"\\author\{.*?\}", r"\\author{\\IEEEauthorblockN{Akash Anipakalu Giridhar}}", tex, flags=re.DOTALL)

parts = tex.split("\\maketitle")
if len(parts) > 1:
    body = parts[1]
    body = re.sub(r"\\section\{Abstract\}", "", body)
    sec_idx = body.find("\\section{")
    if sec_idx != -1:
        abstract_text = body[:sec_idx].strip()
        rest = body[sec_idx:]
        tex = parts[0] + "\\maketitle\n\\begin{abstract}\n" + abstract_text + "\n\\end{abstract}\n\n" + rest

tex, _ = remove_missing_figures(tex, out_dir)

tex_path = out_dir / "paper_akash.tex"
tex_path.write_text(tex, encoding="utf-8")

if (stage19_dir / "references.bib").exists():
    (out_dir / "references.bib").write_text((stage19_dir / "references.bib").read_text(encoding="utf-8"))

print("Compiling pdflatex...")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_akash.tex"], cwd=str(out_dir))
subprocess.run(["bibtex", "paper_akash.aux"], cwd=str(out_dir))
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_akash.tex"], cwd=str(out_dir))
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_akash.tex"], cwd=str(out_dir))
print("Finished!")
