# 🛡️ Wi-Fi Security Hardening Tool

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Linux-Kali%20Linux-black?style=for-the-badge&logo=kalilinux" alt="Kali Linux">
  <img src="https://img.shields.io/badge/Security-Network%20Security-red?style=for-the-badge" alt="Network Security">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>A Python-based network security auditing and hardening tool for authorized Wi-Fi/LAN environments.</b>
</p>

---

## 📌 Overview

The **Wi-Fi Security Hardening Tool** is a Python-based cybersecurity project designed to help users and security students perform a structured security assessment of a local wireless router and connected network.

The tool combines multiple security assessment capabilities into a single command-line application.

It can:

- Detect local network information
- Identify the default gateway/router
- Determine the active network interface
- Audit HTTP and HTTPS router management access
- Perform TCP service auditing
- Discover devices connected to the local network
- Collect router firmware information
- Generate security findings
- Calculate a security score
- Generate a combined JSON security report

The project is designed primarily for **authorized security testing, cybersecurity education, laboratory environments, and defensive network assessment**.

> ⚠️ **Important:** Only use this tool against networks, routers, and devices that you own or have explicit permission to test.

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Automate basic Wi-Fi/router security assessment tasks.
2. Identify potentially exposed router management services.
3. Discover devices connected to the local network.
4. Collect important network and router information.
5. Generate security findings based on observed conditions.
6. Provide a simple security scoring mechanism.
7. Produce a structured security report.
8. Help students understand practical network security auditing.
9. Demonstrate Python-based cybersecurity automation.
10. Provide a foundation for future security-hardening features.

---

# 🚀 Key Features

## 1. 🌐 Network Scanner

The network scanner identifies important information about the current network environment.

### Capabilities

- Detect active network interface
- Detect default gateway
- Determine local network range
- Identify router IP address
- Display network configuration

### Example

```text
[*] Detecting network information...

[+] Interface : eth0
[+] Gateway   : 192.168.1.1
[+] Network   : 192.168.1.0/24


---

## 2. 🔐 Router Security Audit

The router security audit checks whether the router management interface is accessible through HTTP and HTTPS.

### HTTP Audit

The tool checks:

- HTTP connectivity
- HTTP response status
- Server banner
- Redirect behavior

Example:

```text
[+] HTTP Status : 302
[+] Server      : Boa/0.93.15
[+] Location    : /admin/login_en.asp
```

### HTTPS Audit

The tool also checks HTTPS availability.

```text
[+] HTTPS Status : 302
```

> HTTP/HTTPS results should be interpreted together with router configuration, authentication settings, WAN exposure, and firmware status.

---

## 3. 🔎 Service Audit

The service auditing module checks commonly used TCP ports on the router.

| Port | Service | Purpose |
|------|---------|---------|
| 21 | FTP | File Transfer |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Remote Administration |
| 80 | HTTP | Web Management |
| 443 | HTTPS | Secure Web Management |
| 8080 | HTTP Alternative | Alternative Web Service |

### Example

```text
[*] Running service audit...

Port 21   : OPEN
Port 22   : OPEN
Port 23   : CLOSED
Port 80   : OPEN
Port 443  : OPEN
Port 8080  : CLOSED
```

The tool uses these results to generate security findings.

---

## 4. 📱 Device Discovery

The device discovery module identifies devices visible on the local network using ARP-based discovery.

### Information collected

- IP address
- MAC address
- Vendor information

### Example

```text
[+] Devices discovered: 2

- 192.168.1.1 | 98:9d:b2:31:ac:40 | Unknown
- 192.168.1.3 | 98:2c:bc:a7:87:76 | Intel Corporate
```

Duplicate IP/MAC entries are filtered to keep discovery results clean.

---

## 5. 🧩 Firmware Security Check

The firmware module collects router firmware information.

The user provides:

```text
Manufacturer
Router Model
Current Firmware Version
```

Example:

```text
Manufacturer : Syrotech
Model        : SY-GPON-1110-WDONT
Firmware     : v1.0.0
```

The tool records the verification status.

```json
{
    "verification_status": "User-provided"
}
```

### Why firmware matters

Keeping router firmware updated is important because vendors may release updates containing:

- Security fixes
- Vulnerability patches
- Stability improvements
- Performance improvements

> The current implementation records firmware information but does not automatically verify the version against the manufacturer's database.

---

# 6. 🚨 Security Findings

The tool converts audit results into structured security findings.

Example:

```json
{
    "severity": "REVIEW",
    "title": "HTTP management accessible",
    "description": "Router management interface is reachable through HTTP.",
    "recommendation": "Prefer HTTPS management where supported."
}
```

### Severity Levels

| Severity | Meaning |
|----------|---------|
| HIGH | Important security issue requiring attention |
| MEDIUM | Security weakness that should be reviewed |
| REVIEW | Configuration or exposure requiring manual verification |
| LOW | Minor security concern |
| INFO | Informational result |
| PASS | Positive security result |

---

# 7. 📊 Security Scoring

The project includes a simple rule-based security scoring system.

The starting score is:

```text
100
```

Points are deducted according to finding severity.

| Severity | Penalty |
|----------|---------:|
| HIGH | 25 |
| MEDIUM | 15 |
| REVIEW | 10 |
| LOW | 5 |
| INFO | 0 |
| PASS | 0 |

The final score is limited to:

```text
0 - 100
```

### Score Labels

| Score | Label |
|-------|-------|
| 80–100 | Good |
| 60–79 | Needs Improvement |
| 40–59 | Weak |
| 0–39 | Critical Review Required |

### Example

```text
Security score: 70/100 (Needs Improvement)
```

> The score is a simplified educational risk indicator and is not a replacement for a professional security assessment.

---

# 8. 📄 Combined Security Report

The project generates a structured JSON report.

Output file:

```text
security_report.json
```

The report can contain:

- Network information
- Router information
- Security findings
- Service audit results
- Discovered devices
- Firmware information
- Security score
- Score label
- Timestamp

### Example Structure

```json
{
    "audit_type": "Wireless Router Security Audit",
    "timestamp": "YYYY-MM-DD HH:MM:SS",

    "network": {
        "gateway": "192.168.1.1",
        "interface": "eth0",
        "network": "192.168.1.0/24"
    },

    "findings": [],

    "devices": [],

    "services": [],

    "firmware": {},

    "security_score": 85,
    "score_label": "Good"
}
```

---

# 🖥️ Application Menu

The main application provides a simple menu-driven interface.

```text
========================================
      Wi-Fi Security Hardening Tool
========================================

[1] Network Scanner
[2] Complete Router Security Audit
[3] Device Discovery
[4] Generate Combined Security Report
[5] Service Audit
[6] Firmware Security Check
[0] Exit
```

---

# 🏗️ Project Architecture

```text
                    ┌───────────────────────┐
                    │       main.py         │
                    │   Main Application    │
                    └───────────┬───────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
 ┌────────────────┐    ┌────────────────┐    ┌─────────────────┐
 │ Network Scanner│    │ Router Audit   │    │ Service Audit   │
 └───────┬────────┘    └───────┬────────┘    └────────┬────────┘
         │                     │                      │
         ▼                     ▼                      ▼
 ┌────────────────┐    ┌────────────────┐    ┌─────────────────┐
 │ Network Info   │    │ HTTP / HTTPS   │    │ TCP Services    │
 └────────────────┘    └────────────────┘    └─────────────────┘

          ┌─────────────────────┬──────────────────────┐
          │                     │                      │
          ▼                     ▼                      ▼
 ┌────────────────┐    ┌────────────────┐    ┌─────────────────┐
 │ Device         │    │ Firmware       │    │ Security Score  │
 │ Discovery      │    │ Check          │    │                 │
 └───────┬────────┘    └───────┬────────┘    └────────┬────────┘
         │                     │                      │
         └─────────────────────┼──────────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Report Generator     │
                    │                      │
                    │ security_report.json │
                    └──────────────────────┘
```

---

# 📁 Project Structure

```text
wifi-security-hardener-combined/
│
├── main.py
│
├── network_info.py
├── scanner.py
├── audit.py
├── service_audit.py
├── device_discovery.py
├── firmware_check.py
├── security_score.py
├── recommendations.py
├── report_generator.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── security_report.json
```

---

# 🧰 Technologies Used

## Programming Language

- Python 3.x

## Operating System

- Kali Linux
- Linux-based environments

## Security Technologies

- ARP discovery
- TCP service auditing
- HTTP/HTTPS analysis
- Network interface detection
- Router security assessment

## Python Libraries

- Requests
- Scapy
- Python-dotenv
- BeautifulSoup4

## System Tools

- arp-scan
- curl
- Git
- Terminal

---

# ⚙️ Requirements

## Hardware Requirements

### Minimum

- Computer/Laptop
- 4 GB RAM
- 10 GB free storage
- Network interface
- Router/network for authorized testing

### Recommended

- 8 GB+ RAM
- SSD storage
- Ethernet connection
- Dedicated test router

---

# 💻 Software Requirements

Recommended environment:

```text
Operating System : Kali Linux
Python           : Python 3.x
Git              : Latest available version
```

Required system utilities:

```text
arp-scan
curl
```

---

# 📦 Python Dependencies

The project uses the following Python packages:

```text
beautifulsoup4==4.15.0
certifi==2026.7.22
charset-normalizer==3.5.1
idna==3.20
python-dotenv==1.2.3
requests==2.34.2
scapy==2.7.0
soupsieve==2.10
typing_extensions==4.16.0
urllib3==2.8.0
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🚀 Installation

## Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/wifi-security-hardener-combined.git
```

Enter the project directory:

```bash
cd wifi-security-hardener-combined
```

---

## Step 2 — Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

You should see:

```text
(.venv)
```

in your terminal.

---

## Step 3 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Install System Dependencies

On Kali Linux:

```bash
sudo apt update
sudo apt install arp-scan curl
```

Verify:

```bash
arp-scan --version
```

and:

```bash
curl --version
```

---

# ▶️ Running the Project

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run:

```bash
python3 main.py
```

The main menu will appear.

---

# 🔍 Usage

## Option 1 — Network Scanner

Select:

```text
[1] Network Scanner
```

The tool detects:

- Interface
- Gateway
- Local network

---

## Option 2 — Complete Router Security Audit

Select:

```text
[2] Complete Router Security Audit
```

The application performs:

1. Network detection
2. HTTP audit
3. HTTPS audit
4. Service audit
5. Device discovery
6. Firmware information collection
7. Security finding generation
8. Security score calculation
9. Report generation

---

## Option 3 — Device Discovery

Select:

```text
[3] Device Discovery
```

The tool scans the authorized local network and displays detected devices.

Example:

```text
[+] Devices discovered: 2

192.168.1.1
192.168.1.3
```

---

## Option 4 — Generate Combined Report

Select:

```text
[4] Generate Combined Security Report
```

The tool generates:

```text
security_report.json
```

---

## Option 5 — Service Audit

Select:

```text
[5] Service Audit
```

The application checks selected TCP ports on the router.

---

## Option 6 — Firmware Security Check

Select:

```text
[6] Firmware Security Check
```

Enter the router information:

```text
Manufacturer:
Model:
Current Firmware:
```

---

# 🧪 Tested Environment

The project was tested in an authorized local network environment.

Example environment:

```text
Router Manufacturer : Syrotech
Router Model        : SY-GPON-1110-WDONT
Firmware            : v1.0.0
Gateway             : 192.168.1.1
Network             : 192.168.1.0/24
Interface           : eth0
Operating System    : Kali Linux
```

### Observed Router Services

```text
FTP     21    OPEN
SSH     22    OPEN
Telnet  23    CLOSED
HTTP    80    OPEN
HTTPS   443   OPEN
HTTP    8080  CLOSED
```

> These results represent the tested environment and should not be interpreted as universal characteristics of the router model.

---

# 🛡️ Security Hardening Recommendations

## 1. Use HTTPS

Prefer encrypted router management interfaces.

## 2. Disable Unused Services

If FTP, Telnet, SSH, or other services are not required, disable them.

## 3. Change Default Credentials

Use strong, unique administrator credentials.

## 4. Update Firmware

Install security updates from the router manufacturer when available.

## 5. Restrict Management Access

Router administration should ideally be restricted to trusted local devices.

## 6. Disable WAN Management

If remote administration is unnecessary, disable it.

## 7. Use Strong Wi-Fi Security

Prefer modern wireless security standards supported by the router.

## 8. Review Connected Devices

Investigate unknown devices connected to the network.

## 9. Disable WPS When Not Required

If WPS is unnecessary, disabling it can reduce the attack surface.

## 10. Monitor Router Logs

Regularly review authentication and security events when logging is available.

---

# ⚠️ Limitations

The current version has several limitations.

### 1. Local Network Focus

The tool primarily evaluates the local router/network environment.

### 2. No Automatic Vulnerability Exploitation

The project does not exploit vulnerabilities.

### 3. No WAN Exposure Verification

An open local port does not necessarily mean that the service is exposed to the Internet.

### 4. Firmware Verification

Firmware information is currently user-provided and is not automatically verified against the manufacturer's database.

### 5. Device Identification

Vendor information depends on the available MAC/OUI data and network discovery results.

### 6. Security Score

The scoring system is a simplified educational risk model and should not be treated as an industry-standard security rating.

### 7. Wireless Adapter Requirement

Some wireless-specific tests may require a physical Wi-Fi adapter capable of supporting the required operations.

---

# 🔮 Future Enhancements

Potential future improvements include:

- Automatic firmware version verification
- CVE database integration
- CVSS-based vulnerability scoring
- Router vendor identification
- MAC/OUI database integration
- Advanced service fingerprinting
- SSL/TLS configuration analysis
- Wi-Fi encryption detection
- WPS security assessment
- DNS security checks
- DHCP security checks
- Rogue device detection
- Network topology visualization
- HTML report generation
- PDF report generation
- Web dashboard
- Historical security reports
- Automated remediation recommendations
- Scheduled security audits
- Database storage
- Email notifications
- SIEM integration

---

# 🧠 Learning Outcomes

This project demonstrates practical knowledge of:

- Python programming
- Network security
- Linux administration
- Network reconnaissance
- TCP/IP fundamentals
- HTTP/HTTPS
- Router security
- ARP
- Service enumeration
- Device discovery
- Security scoring
- JSON data processing
- Cybersecurity automation
- Security reporting
- Ethical security testing

---

# 🧪 Testing Methodology

Testing was performed using an authorized test network.

The following areas were tested:

| Test | Description |
|------|-------------|
| Network Detection | Gateway and interface detection |
| HTTP Audit | HTTP connectivity and response analysis |
| HTTPS Audit | HTTPS connectivity |
| Service Audit | TCP port checks |
| Device Discovery | Local network device identification |
| Firmware Check | Router firmware information collection |
| Finding Generation | Security finding creation |
| Score Calculation | Security score generation |
| Report Generation | JSON report creation |

---

# 📈 Project Workflow

```text
Start
  │
  ▼
Detect Network
  │
  ▼
Identify Gateway
  │
  ▼
Run Security Checks
  │
  ├───────────────┐
  │               │
  ▼               ▼
HTTP/HTTPS     Services
  │               │
  └───────┬───────┘
          ▼
   Discover Devices
          │
          ▼
   Collect Firmware
          │
          ▼
 Generate Findings
          │
          ▼
 Calculate Score
          │
          ▼
 Generate JSON Report
          │
          ▼
         End
```

---

# 📄 Output Files

The primary generated report is:

```text
security_report.json
```

---

# 🤝 Contributing

Contributions are welcome.

### 1. Fork the repository

Use the **Fork** button on GitHub.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR-USERNAME/wifi-security-hardener-combined.git
```

### 3. Create a branch

```bash
git checkout -b feature/new-security-check
```

### 4. Make your changes

Implement and test your changes.

### 5. Commit

```bash
git add .
git commit -m "Add new security check"
```

### 6. Push

```bash
git push origin feature/new-security-check
```

### 7. Create a Pull Request

Submit your changes for review.

---

# 🐛 Bug Reports

If you discover a bug, please provide:

- Operating system
- Python version
- Error message
- Steps to reproduce
- Expected behavior
- Actual behavior

Please avoid sharing:

- Router passwords
- API keys
- Sensitive network configuration
- Personal information

---

# 🔐 Responsible Disclosure

If a security vulnerability is discovered in this project, please report it responsibly rather than publicly publishing exploit details immediately.

Provide:

- Vulnerability description
- Affected component
- Reproduction steps
- Potential impact
- Suggested mitigation

---

# 📜 License

This project is intended for educational and authorized security-testing purposes.

A suitable open-source license can be added to the repository depending on the intended distribution model.

---

# 👨‍💻 Author

## Nandhakumar

Cybersecurity Engineering Student

### Areas of Interest

- 🔐 Cybersecurity
- 🌐 Network Security
- 🛡️ Ethical Hacking
- ⚙️ Security Automation
- 🔎 Penetration Testing
- 🚨 SOC Operations

---

# ⭐ Support the Project

If you find this project useful for learning cybersecurity:

⭐ Star the repository

🍴 Fork the repository

🐛 Report bugs

💡 Suggest improvements

🤝 Contribute to the project

---

# 📚 References

Useful cybersecurity resources:

- OWASP
- NIST Cybersecurity Framework
- MITRE ATT&CK
- CVE / NVD
- Python Documentation
- Scapy Documentation
- Kali Linux Documentation

---

# ⚠️ Disclaimer

This tool is provided for educational and defensive security purposes.

Only perform security testing against systems and networks that you own or have explicit authorization to assess.

The author does not encourage unauthorized scanning, exploitation, intrusion, credential attacks, or disruption of networks and systems.

Use responsibly.

---

<p align="center">
  <b>🛡️ Wi-Fi Security Hardening Tool</b>
  <br>
  Built with Python for Cybersecurity Education & Authorized Network Security Assessment
</p>
```