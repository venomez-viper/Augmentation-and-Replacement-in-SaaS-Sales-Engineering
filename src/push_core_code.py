import shutil
from pathlib import Path
import subprocess

src = Path("C:/Users/akash/Desktop/Research/AutoResearchClaw")
dst = Path("C:/Users/akash/Desktop/Research/Augmentation-and-Replacement-in-SaaS-Sales-Engineering/AutoResearchClaw")

dst.mkdir(parents=True, exist_ok=True)

def ignore_func(dir_path, contents):
    ignores = ['.git', '.venv', '__pycache__', '.claude', 'test_outputs', '.pytest_cache']
    return [c for c in contents if c in ignores or c.endswith('.pyc') or c.startswith('.')]

shutil.copytree(src, dst, ignore=ignore_func, dirs_exist_ok=True)

subprocess.run(["git", "add", "."], cwd=str(dst.parent))
subprocess.run(["git", "commit", "-m", "Upload complete AutoResearchClaw experiment pipeline and raw artifacts"], cwd=str(dst.parent))
subprocess.run(["git", "push", "origin", "main"], cwd=str(dst.parent))
print("Successfully pushed the core research code to Github!")
