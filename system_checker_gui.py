import platform
import psutil
import socket
import subprocess
import requests
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Official speedtest-cli import
try:
    import speedtest
except ImportError:
    speedtest = None

# ---------- FUNCTIONS ----------

def generate_report(email):
    report_lines = []

    # System info
    os_name = platform.system()
    os_version = platform.version()
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_lines.append(f"Email: {email}")
    report_lines.append(f"Operating System: {os_name}")
    report_lines.append(f"OS Version: {os_version}")
    report_lines.append(f"Hostname: {hostname}")

    # CPU cores
    cores = psutil.cpu_count(logical=False)
    report_lines.append(f"CPU Cores: {cores}")
    report_lines.append("CPU Requirement: MEETS ✅" if cores >= 7 else "CPU Requirement: FAIL ❌")

    # RAM
    ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
    report_lines.append(f"RAM (GB): {ram_gb}")
    report_lines.append("RAM Requirement: MEETS ✅" if ram_gb >= 15 else "RAM Requirement: FAIL ❌")

    # Network connection
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        report_lines.append("Network: Connected ✅")
    except:
        report_lines.append("Network: Not Connected ❌")

    # Speed test
    if speedtest:
        try:
            st = speedtest.Speedtest()
            download = round(st.download() / 1_000_000, 2)
            upload = round(st.upload() / 1_000_000, 2)
            report_lines.append(f"Download: {download} Mbps")
            report_lines.append("Download Requirement: MEETS ✅" if download >= 40 else "Download Requirement: FAIL ❌")
            report_lines.append(f"Upload: {upload} Mbps")
            report_lines.append("Upload Requirement: MEETS ✅" if upload >= 15 else "Upload Requirement: FAIL ❌")
        except Exception as e:
            report_lines.append(f"Speed Test Failed ❌ ({e})")
    else:
        report_lines.append("Speed Test Skipped ❌ (speedtest-cli missing)")

    # TPM check (Windows)
    if os_name == "Windows":
        try:
            result = subprocess.run(["powershell", "Get-Tpm"], capture_output=True, text=True)
            if "TpmPresent" in result.stdout:
                report_lines.append("TPM: Detected ✅ (Win11 Compatible)")
            else:
                report_lines.append("TPM: Not Detected ❌")
        except:
            report_lines.append("TPM Check Failed ❌")

    # IP & country
    try:
        public_ip = requests.get("https://api.ipify.org").text
        geo = requests.get(f"http://ip-api.com/json/{public_ip}").json()
        report_lines.append(f"Public IP: {public_ip}")
        report_lines.append(f"Country: {geo.get('country')}")
        report_lines.append("VPN/Proxy: Detected ❌" if geo.get("proxy") else "VPN/Proxy: Not Detected ✅")
    except:
        report_lines.append("Country/VPN Check Failed ❌")

    report_lines.append(f"Report Generated: {current_date}")

    return report_lines

def save_pdf(report_lines):
    # Get Desktop path
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create Desktop folder if it doesn't exist
    if not os.path.exists(desktop):
        try:
            os.makedirs(desktop)
        except Exception as e:
            # Fallback to current directory if Desktop not available
            print(f"Could not access Desktop, saving in current folder: {e}")
            desktop = os.getcwd()

    file_name = os.path.join(desktop, "System_Report.pdf")
    doc = SimpleDocTemplate(file_name)
    elements = []
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    for line in report_lines:
        elements.append(Paragraph(line, normal_style))
        elements.append(Spacer(1, 0.2*inch))

    doc.build(elements)
    return file_name

def run_check():
    email = email_entry.get().strip()
    if not email:
        messagebox.showerror("Error", "Please enter your email")
        return

    report = generate_report(email)
    file_name = save_pdf(report)

    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)
    for line in report:
        result_text.insert(tk.END, line + "\n")
    result_text.config(state='disabled')

    messagebox.showinfo("Success", f"Report saved to: {file_name}")

# ---------- GUI ----------

root = tk.Tk()
root.title("System Checker")
root.geometry("700x600")

tk.Label(root, text="Enter your Email:").pack(pady=10)
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

tk.Button(root, text="Run System Check", command=run_check).pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=80, height=25, state='disabled')
result_text.pack(padx=10, pady=10)

tk.Button(root, text="Close", command=root.destroy, bg="red", fg="white").pack(pady=10)

root.mainloop()