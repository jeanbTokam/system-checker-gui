# System Checker GUI

A Python GUI application to check your system’s specifications, network performance, and compatibility requirements. The app collects system info, performs network speed tests, checks CPU, RAM, TPM (for Windows), and generates a PDF report.

---

## **Objectives**

- Verify system hardware requirements (CPU cores ≥ 7, RAM ≥ 15GB).
- Test network connectivity and speed (Download ≥ 40 Mbps, Upload ≥ 15 Mbps).
- Detect TPM presence for Windows 11 compatibility.
- Collect IP and country info and detect VPN/proxy.
- Generate a detailed PDF report saved on the Desktop.
- Provide a GUI for user-friendly interaction.

---

## **Requirements & Tools**

- **Python 3.10+** (Python 3.14 recommended)  
- **Packages:**  
  - `psutil` – system and hardware info  
  - `speedtest-cli` – network speed test  
  - `requests` – IP and geolocation info  
  - `tkinter` – GUI interface (comes with Python)  
  - `reportlab` – generate PDF report  

- **Optional:** Windows PowerShell (for TPM detection)

---

## **Installation Steps**

1. **Clone or download** the project repository:  

```bash
git clone https://github.com/YourUsername/system-checker-gui.git
cd system-checker-gui
![]("C:\Users\jbtok\OneDrive\Pictures\Screenshots\System check.png")