import re
from pathlib import Path
from researchclaw.templates import get_template, markdown_to_latex

run_dir = Path("artifacts/rc-20260330-061112-a2ffee")
stage19_dir = run_dir / "stage-19"
out_dir = run_dir / "deliverables"

md_content = (stage19_dir / "paper_revised.md").read_text(encoding="utf-8")

md_content = re.sub(r"^#+\s*Abstract", "", md_content, flags=re.MULTILINE|re.IGNORECASE)

tpl = get_template("generic")
tex = markdown_to_latex(
    md_content, 
    tpl, 
    title="APEX: AI Augments or Replaces — Measuring SaaS Presales Role Survival",
    authors=["Akash"], 
    bib_file="references.bib"
)

tex = tex.replace("\\documentclass{article}", "\\documentclass[10pt, conference]{IEEEtran}")
tex = re.sub(r"\\usepackage(?:\[.*?\])?\{geometry\}", "", tex)

parts = tex.split("\\maketitle")
if len(parts) > 1:
    body = parts[1]
    sec_idx = body.find("\\section{")
    if sec_idx != -1:
        abstract_text = body[:sec_idx].strip()
        rest = body[sec_idx:]
        tex = parts[0] + "\\maketitle\n\\begin{abstract}\n" + abstract_text + "\n\\end{abstract}\n\n" + rest

tex = re.sub(r"(?<!\$)\\mathcal\{([^\}]+)\}(?!\$)", r"$\\mathcal{\1}$", tex)
tex = re.sub(r" (?<!\\)& ", r" \\& ", tex)

out_dir.mkdir(parents=True, exist_ok=True)
tex_path = out_dir / "paper.tex"
tex_path.write_text(tex, encoding="utf-8")
print("Wrote paper.tex successfully!")
