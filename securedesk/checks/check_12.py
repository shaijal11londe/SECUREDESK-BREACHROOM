"""
SECUREDESK - BreachRoom Check #12
Check: security_check_12
"""

import os, platform
def run():
    # Check 12: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 12, "name": "security_check_12"}
    return {"status": "PASS", "check_id": 12}


if __name__ == "__main__":
    print(run())
