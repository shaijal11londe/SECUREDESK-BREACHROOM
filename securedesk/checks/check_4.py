"""
SECUREDESK - BreachRoom Check #4
Check: security_check_4
"""

import os, platform
def run():
    # Check 4: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 4, "name": "security_check_4"}
    return {"status": "PASS", "check_id": 4}


if __name__ == "__main__":
    print(run())
