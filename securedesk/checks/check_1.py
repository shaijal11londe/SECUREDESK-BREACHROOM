"""
SECUREDESK - BreachRoom Check #1
Check: firewall_status
"""

import subprocess
def run():
    try:
        result = subprocess.getoutput("netsh advfirewall show allprofiles state")
        if "ON" in result: return {"status": "PASS", "msg": "Firewall ON"}
        return {"status": "FAIL", "msg": "Firewall OFF"}
    except Exception as e:
        return {"status": "FAIL", "msg": str(e)}


if __name__ == "__main__":
    print(run())
