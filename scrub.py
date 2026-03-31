import os
from pathlib import Path
import subprocess

root = Path(r"C:\Users\akash\Desktop\Research\Augmentation-and-Replacement-in-SaaS-Sales-Engineering")
ignore_exts = {".pdf", ".png", ".jpg", ".tar", ".gz", ".zip"}

# 1. Text Replacement
count = 0
for p in root.rglob("*"):
    if p.is_file() and ".git" not in p.parts:
        if p.suffix.lower() in ignore_exts: continue
        try:
            text = p.read_text(encoding="utf-8")
            new_text = text.replace("ResearchPipeline", "ResearchPipeline")
            new_text = new_text.replace("researchpipeline", "researchpipeline")
            new_text = new_text.replace("researchpipeline", "researchpipeline")
            new_text = new_text.replace("ResearchPipeline", "ResearchPipeline")
            new_text = new_text.replace("Research Pipeline", "Research Pipeline")
            if text != new_text:
                p.write_text(new_text, encoding="utf-8")
                count += 1
        except UnicodeDecodeError:
            pass

print(f"Replaced text in {count} files.")

# 2. Directory/File Renaming (bottom-up to avoid path invalidation)
rename_count = 0
for p in sorted(root.rglob("*"), key=lambda x: len(x.parts), reverse=True):
    if ".git" in p.parts:
        continue
    name = p.name
    new_name = name.replace("ResearchPipeline", "ResearchPipeline")
    new_name = new_name.replace("researchpipeline", "researchpipeline")
    new_name = new_name.replace("researchpipeline", "researchpipeline")
    new_name = new_name.replace("ResearchPipeline", "ResearchPipeline")
    
    if name != new_name:
        new_path = p.with_name(new_name)
        p.rename(new_path)
        rename_count += 1

print(f"Renamed {rename_count} paths.")

# 3. Commit and Push
subprocess.run(["git", "add", "."], cwd=str(root))
subprocess.run(["git", "commit", "-m", "Scrub framework branding from all code files and paths"], cwd=str(root))
subprocess.run(["git", "push", "origin", "main"], cwd=str(root))
print("Scrub and Push complete!")
