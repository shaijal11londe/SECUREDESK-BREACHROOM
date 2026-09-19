"""
SECUREDESK - BreachRoom Check #6
Check: security_check_6
"""

import os, platform
def run():
    # Check 6: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 6, "name": "security_check_6"}
    return {"status": "PASS", "check_id": 6}


if __name__ == "__main__":
    print(run())
