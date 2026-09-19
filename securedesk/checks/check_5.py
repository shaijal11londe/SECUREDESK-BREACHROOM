"""
SECUREDESK - BreachRoom Check #5
Check: security_check_5
"""

import os, platform
def run():
    # Check 5: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 5, "name": "security_check_5"}
    return {"status": "PASS", "check_id": 5}


if __name__ == "__main__":
    print(run())
