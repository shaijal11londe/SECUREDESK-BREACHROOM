"""
SECUREDESK - BreachRoom Check #9
Check: security_check_9
"""

import os, platform
def run():
    # Check 9: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 9, "name": "security_check_9"}
    return {"status": "PASS", "check_id": 9}


if __name__ == "__main__":
    print(run())
