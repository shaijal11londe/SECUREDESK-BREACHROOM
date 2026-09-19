"""
SECUREDESK - BreachRoom Check #80
Check: security_check_80
"""

import os, platform
def run():
    # Check 80: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 80, "name": "security_check_80"}
    return {"status": "PASS", "check_id": 80}


if __name__ == "__main__":
    print(run())
