import subprocess

with open("build.log", "r", errors="ignore") as f:
    logs = f.read()[-3000:]

prompt = f"""
You are a DevOps expert.
Analyze Jenkins build failure logs.
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

print("\n====== AI BUILD FAILURE ANALYSIS ======\n")
print(result.stdout)
print("\n======================================\n")
