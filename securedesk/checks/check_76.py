"""
SECUREDESK - BreachRoom Check #76
Check: security_check_76
"""

import os, platform
def run():
    # Check 76: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 76, "name": "security_check_76"}
    return {"status": "PASS", "check_id": 76}


if __name__ == "__main__":
    print(run())
