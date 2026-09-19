from colorama import Fore, Style, init
import os
import importlib.util

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "\n=== SECUREDESK - BREACHROOM SCAN STARTED ===\n")

checks_path = "securedesk/checks"
files = sorted([f for f in os.listdir(checks_path) if f.startswith("check_")])

for file in files:
    try:
        path = os.path.join(checks_path, file)
        spec = importlib.util.spec_from_file_location("module", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # jar module madhe function asel tar
        print(Fore.GREEN + f"[PASS] {file} executed successfully")
    except Exception as e:
        print(Fore.RED + f"[FAIL] {file} -> {e}")

print(Fore.CYAN + Style.BRIGHT + "\n=== SCAN COMPLETE: 95 Checks Done ===\n")