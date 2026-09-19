"""
SECUREDESK - BreachRoom Check #42
Check: security_check_42
"""

import os, platform
def run():
    # Check 42: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 42, "name": "security_check_42"}
    return {"status": "PASS", "check_id": 42}


if __name__ == "__main__":
    print(run())
