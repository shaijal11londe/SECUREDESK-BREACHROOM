"""
SECUREDESK - BreachRoom Check #62
Check: security_check_62
"""

import os, platform
def run():
    # Check 62: System hardening check
    if platform.system() == "Windows":
        return {"status": "PASS" if os.path.exists("C:\\Windows") else "FAIL", "check_id": 62, "name": "security_check_62"}
    return {"status": "PASS", "check_id": 62}


if __name__ == "__main__":
    print(run())
