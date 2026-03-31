from markdown_pdf import MarkdownPdf
from markdown_pdf import Section
from pathlib import Path

run_dir = Path("artifacts/rc-20260330-061112-a2ffee")
stage19_dir = run_dir / "stage-19"
out_dir = run_dir / "deliverables"

md_content = (stage19_dir / "paper_revised.md").read_text(encoding="utf-8")

pdf = MarkdownPdf(toc_level=2)
pdf.add_section(Section(md_content))
pdf.save(str(out_dir / "paper.pdf"))
print("Final PDF generated successfully!")
