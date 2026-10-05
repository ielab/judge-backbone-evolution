import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import sys

# Ensure execution from the repository root
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
    return result.returncode

commands = []

# For 3.5, 3.6, 3.7 -> run1, run2, run3
for model in ["gemini-3.5-flash", "gemini-3.6-flash", "gemini-3.7-flash"]:
    for run_id in [1, 2, 3]:
        commands.append(f"python src/evaluate_trec_dl.py --provider gemini --model {model} --workers 16 --run_id {run_id} --output_dir results/repeats_no_thinking")

# For 2.5, 3.8 -> run2, run3
for model in ["gemini-2.5-flash", "gemini-3.8-flash"]:
    for run_id in [2, 3]:
        commands.append(f"python src/evaluate_trec_dl.py --provider gemini --model {model} --workers 16 --run_id {run_id} --output_dir results/repeats_no_thinking")

if __name__ == "__main__":
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not set in environment.")
        sys.exit(1)
        
    print(f"Launching {len(commands)} runs with max concurrency 2")
    with ThreadPoolExecutor(max_workers=2) as executor:
        list(executor.map(run_command, commands))
    print("All runs finished.")
