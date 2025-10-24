# SteamVR Battery Checker 🔋

A simple Python script to check the battery level of SteamVR devices (headset, controllers, base stations) using the **OpenVR** library.

---

## 🧰 Features
- Lists all devices connected to SteamVR  
- Displays the current battery percentage (if available)  
- Works with Vive, Index, Quest Link, and other OpenVR-compatible devices  

---

## 🚀 Requirements
- **Python 3.10+**  
- **openvr** library

Install dependencies:
```bash
pip install openvr


How to Run

Start SteamVR

Run the script in your terminal or PowerShell:

python steamvr_battery.py


You’ll see a list of connected devices and their battery levels:

0: HMD (LHR-XXXXXXX) – battery: 95%
1: Controller (LHR-YYYYYYY) – battery: 81%
2: Controller (LHR-ZZZZZZZ) – no battery data
