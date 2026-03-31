import sys
from pathlib import Path
from researchclaw.templates import get_template, markdown_to_latex
from researchclaw.templates.compiler import compile_latex

run_dir = Path("artifacts/rc-20260330-061112-a2ffee")
stage19_dir = run_dir / "stage-19"
out_dir = run_dir / "deliverables"

print("Reading parsed markdown...")
md_content = (stage19_dir / "paper_revised.md").read_text(encoding="utf-8")

print("Generating LaTeX...")
tpl = get_template("neurips_2025")
tex_content = markdown_to_latex(
    md_content, 
    tpl, 
    title="APEX: AI Augments or Replaces — Measuring SaaS Presales Role Survival",
    authors=["Akash"], 
    bib_file="references.bib"
)

tex_path = out_dir / "paper.tex"
tex_path.write_text(tex_content, encoding="utf-8")

# copy style files
for sf in tpl.get_style_files():
    (out_dir / sf.name).write_bytes(sf.read_bytes())
    
# copy bibliography
if (stage19_dir / "references.bib").exists():
    (out_dir / "references.bib").write_text((stage19_dir / "references.bib").read_text(encoding="utf-8"))
elif (run_dir / "references.bib").exists():
    (out_dir / "references.bib").write_text((run_dir / "references.bib").read_text(encoding="utf-8"))
else:
    print("Warning: references.bib not found in run_dir")

# Optional: strip missing charts
try:
    from researchclaw.templates.compiler import remove_missing_figures
    _fixed_tex, _removed_figs = remove_missing_figures(tex_content, out_dir)
    if _removed_figs:
        tex_path.write_text(_fixed_tex, encoding="utf-8")
        print(f"Removed missing figures: {_removed_figs}")
except Exception as e:
    print(f"Fig strip error: {e}")

print("Compiling LaTeX...")
result = compile_latex(tex_path, max_attempts=2)
print("Success:", result.success)
if not result.success:
    print("Errors:", result.errors)
