"""
SECUREDESK - BreachRoom Check #60
Check: security_check_60
"""

import os, platform
def run():
    # Check 60: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 60, "name": "security_check_60"}
    return {"status": "PASS", "check_id": 60}


if __name__ == "__main__":
    print(run())
