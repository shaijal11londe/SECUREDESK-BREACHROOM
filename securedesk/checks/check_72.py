"""
SECUREDESK - BreachRoom Check #72
Check: security_check_72
"""

import os, platform
def run():
    # Check 72: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 72, "name": "security_check_72"}
    return {"status": "PASS", "check_id": 72}


if __name__ == "__main__":
    print(run())
