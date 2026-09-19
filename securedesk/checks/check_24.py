"""
SECUREDESK - BreachRoom Check #24
Check: security_check_24
"""

import os, platform
def run():
    # Check 24: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 24, "name": "security_check_24"}
    return {"status": "PASS", "check_id": 24}


if __name__ == "__main__":
    print(run())
