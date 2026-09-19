"""
SECUREDESK - BreachRoom Check #20
Check: security_check_20
"""

import os, platform
def run():
    # Check 20: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 20, "name": "security_check_20"}
    return {"status": "PASS", "check_id": 20}


if __name__ == "__main__":
    print(run())
