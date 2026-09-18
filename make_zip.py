import os, shutil
if os.path.exists("securedesk"):
    if os.path.isdir("securedesk"):
        shutil.rmtree("securedesk", ignore_errors=True)
    else:
        os.remove("securedesk")

os.makedirs("securedesk/checks", exist_ok=True)
for i in range(95):
    with open(f"securedesk/checks/check_{i}.py","w") as f:
        f.write(f"# File {i}\n")
        for j in range(1000):
            f.write(f"def check_{i}_{j}(): return {j}\n")
print("95 files ready")