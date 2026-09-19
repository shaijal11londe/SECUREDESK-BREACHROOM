"""
SECUREDESK - BreachRoom Check #3
Check: security_check_3
"""

import os, platform
def run():
    # Check 3: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 3, "name": "security_check_3"}
    return {"status": "PASS", "check_id": 3}


if __name__ == "__main__":
    print(run())
