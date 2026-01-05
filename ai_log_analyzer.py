import subprocess
import os

log_file = "build.log"

if not os.path.exists(log_file):
    logs = "Jenkins build failed due to non-zero exit code."
else:
    with open(log_file, "r", errors="ignore") as f:
        logs = f.read()[-3000:]

prompt = f"""
You are a DevOps expert.
Analyze Jenkins failure logs.
Give:
1. Root cause
2. Fix suggestion

Logs:
{logs}
"""

result = subprocess.run(
    ["ollama", "run", "phi3", prompt],
    capture_output=True,
    text=True
)

print("\n=== AI FAILURE ANALYSIS ===\n")
print(result.stdout)
print("\n==========================\n")
