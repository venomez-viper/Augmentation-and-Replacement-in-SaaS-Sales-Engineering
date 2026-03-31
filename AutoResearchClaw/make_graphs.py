import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import subprocess
import re

out_dir = Path("artifacts/rc-20260330-061112-a2ffee/deliverables")
charts_dir = out_dir / "charts"
charts_dir.mkdir(exist_ok=True, parents=True)

# Data from Table 4 in paper_revised.md
conditions = ["C24", "CAB", "AFC", "PAR", "HAO", "FAR"]
means = [0.5124, 0.4541, 0.2890, 0.2173, 0.1448, 0.0091]
stds = [0.0142, 0.0081, 0.0041, 0.0020, 0.0001, 0.0003]

plt.style.use('seaborn-v0_8-whitegrid')
colors = ['#4477AA', '#4477AA', '#228833', '#228833', '#EE6677', '#EE6677']

# Chart 1: RSI Bar Chart
fig, ax = plt.subplots(figsize=(7, 4.5))
x = np.arange(len(conditions))
ax.bar(x, means, yerr=stds, color=colors, capsize=5, alpha=0.85, edgecolor='black')
ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.set_ylabel("Role Survival Index (RSI)")
ax.set_title("RSI Comparison Across AI Adoption Conditions")
ax.set_ylim(0, 0.6)
for i, mean in enumerate(means):
    ax.text(i, mean + stds[i] + 0.015, f"{mean:.3f}", ha='center', fontweight='bold')
fig.tight_layout()
fig.savefig(charts_dir / "rsi_bar_chart.png", dpi=300)
plt.close(fig)

# Chart 2: Seed Sensitivity
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(x, stds, marker='o', color='#AA3377', linewidth=2, markersize=8)
ax.fill_between(x, stds, color='#AA3377', alpha=0.1)
ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.set_ylabel("Seed Standard Deviation")
ax.set_title("Seed Sensitivity per Condition")
ax.set_ylim(0, 0.018)
for i, std in enumerate(stds):
    ax.text(i, std + 0.0005, f"{std:.4f}", ha='center', fontsize=9)
fig.tight_layout()
fig.savefig(charts_dir / "seed_sensitivity.png", dpi=300)
plt.close(fig)

# Now, we need to read the pristine `paper_akash.tex`, but WAIT! I stripped \includegraphics in `paper_akash.tex`.
# So let's re-generate the pristine TEX from markdown!
md_content = Path("artifacts/rc-20260330-061112-a2ffee/stage-19/paper_revised.md").read_text(encoding="utf-8")
md_content = md_content.replace(" —", ":")
md_content = md_content.replace("—", "-")
md_content = md_content.replace("APEX: AI Augments or Replaces:", "APEX: AI Augments or Replaces:")
md_content = re.sub(r"\|.*\|.*\n\|(?:[-\s:]+)\|.*\n(?:\|.*\|.*\n)+", "\n\\textbf{[Table Omitted]}\n\n", md_content, flags=re.MULTILINE)
md_content = re.sub(r"\\alpha\\_k", "alpha-k", md_content)
md_content = re.sub(r"\\beta\\_k\\\$", "beta-k", md_content)

from researchclaw.templates import get_template, markdown_to_latex
tpl = get_template("generic")
tex = markdown_to_latex(md_content, tpl, title="APEX", authors=["Akash Anipakalu Giridhar"], bib_file="references.bib")

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

# We DO NOT run `remove_missing_figures` this time, because the figures EXACTLY match the expected paths!
tex_path = out_dir / "paper_graphs.tex"
tex_path.write_text(tex, encoding="utf-8")

print("Compiling pdflatex...")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_graphs.tex"], cwd=str(out_dir))
subprocess.run(["bibtex", "paper_graphs.aux"], cwd=str(out_dir))
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_graphs.tex"], cwd=str(out_dir))
subprocess.run(["pdflatex", "-interaction=nonstopmode", "paper_graphs.tex"], cwd=str(out_dir))
print("Finished compiling paper_graphs.pdf!")
