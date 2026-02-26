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

python -m venv .venv


---

# 🖥️ System Checker GUI  
A simple cross‑platform system diagnostic tool that checks hardware, network, and security requirements, then generates a clean PDF report.

---

## 🚀 Features  
The application performs a full system check and reports:

- Entered email  
- Operating System & version  
- Hostname  
- CPU cores + requirement status  
- RAM amount + requirement status  
- Network connectivity  
- Download & Upload speeds + requirement checks  
- TPM status (Windows only)  
- Public IP, country lookup, VPN/proxy detection  
- Timestamp of report generation  
- PDF report saved automatically to the Desktop  

---

## 📦 Installation

### 1. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

### 3. Install required packages

Using `requirements.txt`:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install psutil speedtest-cli requests reportlab
```

---

## ▶️ How to Run

Make sure your virtual environment is activated, then run:

```bash
python system_checker_gui.py
```

1. Enter your email in the GUI  
2. Click **“Run System Check”**  
3. Results will appear directly in the GUI  
4. A PDF report will be saved to your Desktop  

---

## 📄 PDF Report Contents

The generated report includes:

- Email entered in the GUI  
- OS name and version  
- Hostname  
- CPU core count + pass/fail  
- RAM amount + pass/fail  
- Internet connectivity  
- Download & upload speeds + requirement checks  
- TPM status (Windows only)  
- Public IP, country, VPN/proxy detection  
- Date & time of report generation  

---

## 🛠️ Requirements

- Python 3.8+  
- Internet connection (for speed test & IP lookup)  
- Windows, macOS, or Linux  
- TPM check works only on Windows  

---

## 📁 Project Structure (example)

```
├── system_checker_gui.py
├── requirements.txt
├── README.md
└── assets/
```

---


<img width="1407" height="934" alt="System check" src="https://github.com/user-attachments/assets/0e9f6128-468c-49c6-a00d-d6a1fd195714" />


## 🤝 Contributing  
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to improve.

---





