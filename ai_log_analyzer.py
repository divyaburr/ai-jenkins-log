import subprocess
import os

LOG_FILE = "build.log"

# 1️⃣ Read logs safely
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        logs = f.read()[-3000:]
else:
    logs = "Jenkins build failed due to non-zero exit code."

# 2️⃣ AI Prompt
prompt = f"""
You are a DevOps expert.

Analyze the Jenkins failure logs below and provide:
1. Root cause
2. Fix suggestion

Logs:
{logs}
"""

# 3️⃣ Start Ollama (NO prompt in args)
process = subprocess.Popen(
    [
        r"C:\Users\SYR00347\AppData\Local\Programs\Ollama\ollama.exe",
        "run",
        "phi"
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

# 4️⃣ Send prompt ONCE
output, error = process.communicate(prompt)

print("\n=== AI FAILURE ANALYSIS ===\n")
print(output.strip())
print("\n==========================\n")
