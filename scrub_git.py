import subprocess
import os

result = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
files = result.stdout.splitlines()

for f in sorted(files, key=len, reverse=True):
    if "researchclaw" in f or "ResearchClaw" in f or "AutoResearchClaw" in f:
        new_f = f.replace("AutoResearchClaw", "ResearchPipeline").replace("researchclaw", "researchpipeline").replace("ResearchClaw", "ResearchPipeline")
        
        os.makedirs(os.path.dirname(new_f), exist_ok=True)
        subprocess.run(["git", "mv", f, new_f])

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Scrub research framework branding from files and paths"])
subprocess.run(["git", "push", "origin", "main"])
print("Git scrub and push complete!")
