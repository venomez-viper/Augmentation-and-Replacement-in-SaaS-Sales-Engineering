import re
import subprocess
from pathlib import Path
from researchpipeline.templates import get_template, markdown_to_latex

run_dir = Path("artifacts/rc-20260330-061112-a2ffee")
stage19_dir = run_dir / "stage-19"
out_dir = run_dir / "deliverables"

md_content = (stage19_dir / "paper_revised.md").read_text(encoding="utf-8")

# 1. Expand APEX
md_content = md_content.replace("APEX addresses this gap by introducing", "The AI Presales Exposure Index (APEX) addresses this gap by introducing")

# 2. Add Acknowledgements
md_content += "\n\n# Acknowledgments\n\nThe author proudly mentions that they used advanced AI and automated research pipelines to learn and conduct this rigorous research work."

# 3. Safely remove specific problematic math variables from markdown
md_content = md_content.replace("$\\alpha_k$", "alpha-k")
md_content = md_content.replace("$\\beta_k$", "beta-k")

# Strip tables to prevent LaTeX alignment errors
md_content = re.sub(r"\|.*\|.*\n\|(?:[-\s:]+)\|.*\n(?:\|.*\|.*\n)+", "\n\\textbf{[Table Omitted]}\n\n", md_content, flags=re.MULTILINE)

tpl = get_template("generic")
tex = markdown_to_latex(
    md_content, 
    tpl, 
    title="The AI Presales Exposure Index (APEX): Augmentation and Replacement in SaaS Sales Engineering",
    authors=["Akash Anipakalu Giridhar"], 
    bib_file="references.bib"
)

# Switch to IEEEtran
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

tex_path = out_dir / "paper_akash_proud.tex"
tex_path.write_text(tex, encoding="utf-8")

print("Compiling pdflatex...")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_akash_proud.tex"], cwd=str(out_dir))
subprocess.run(["bibtex", "paper_akash_proud.aux"], cwd=str(out_dir))
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_akash_proud.tex"], cwd=str(out_dir))
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_akash_proud.tex"], cwd=str(out_dir))
print("Finished!")
