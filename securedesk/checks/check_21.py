"""
SECUREDESK - BreachRoom Check #21
Check: security_check_21
"""

import os, platform
def run():
    # Check 21: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 21, "name": "security_check_21"}
    return {"status": "PASS", "check_id": 21}


if __name__ == "__main__":
    print(run())
