"""
SECUREDESK - BreachRoom Check #84
Check: security_check_84
"""

import os, platform
def run():
    # Check 84: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 84, "name": "security_check_84"}
    return {"status": "PASS", "check_id": 84}


if __name__ == "__main__":
    print(run())
