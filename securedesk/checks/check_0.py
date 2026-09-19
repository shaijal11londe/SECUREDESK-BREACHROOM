"""
SECUREDESK - BreachRoom Check #0
Check: antivirus_status
"""

import psutil
def run():
    for proc in psutil.process_iter(['name']):
        if 'defender' in proc.info['name'].lower() or 'avp' in proc.info['name'].lower():
            return {"status": "PASS", "msg": "Antivirus running"}
    return {"status": "FAIL", "msg": "Antivirus not found"}


if __name__ == "__main__":
    print(run())
