# 🔍 ThreatAware Scanner

ThreatAware Scanner is a powerful, beginner-friendly cybersecurity tool built with **Streamlit** that performs:

- ✅ Port Scanning
- ✅ Shodan Threat Intelligence
- ✅ CVE Vulnerability Checks
- ✅ Geolocation & ASN Lookups
- ✅ Interactive Map View
- ✅ User Authentication
- ✅ Real-time Notifications (Email/Webhook)
- ✅ Multi-Target Scanning
- ✅ SIEM Integration

> ⚠️ This tool is for **educational and authorized security testing purposes only**.

---

## 🖼️ Live Preview (Optional)
[Demo Screenshot or Link here]

---

## 🚀 Features

### ✅ Port Scanner  
Scans common TCP ports (22, 80, 443, etc.) to check if they're open.

### 🛰️ Shodan Integration  
Fetches real-time data from Shodan including:
- Open Ports
- OS Detection
- Services
- Known Vulnerabilities (CVEs)

### 🛡️ CVE Vulnerability Lookup  
Checks open ports/services against known CVEs for high-risk threats.

### 🌍 Geolocation & ASN Info  
Visual map display and metadata about the IP's:
- Country, Region, City  
- ISP, Organization, ASN

### 🔔 Real-Time Notifications  
Get alerts by:
- Email (SMTP)
- Webhook (Slack, Discord, etc.)

### 👥 User Authentication  
Secure login for multiple users with profile support.

### 📦 Multi-Target Scanning  
Scan a list of IPs/domains with summary results.

### 🌐 Interactive Network Map  
Graph view of all scanned nodes and port connections.

### 📊 SIEM Integration  
Export data to JSON/CSV for integration with enterprise tools (e.g., Splunk, Elastic).

---

## 🛠️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/alvi2356/ThreatAwareScanner.git
cd ThreatAwareScanner
ThreatAwareScanner/
│
├── app.py                          # Main Streamlit UI
├── port_scanner_with_shodan.py    # Core scanner and API functions
├── requirements.txt               # Python dependencies
├── logo.png                       # App logo
├── README.md                      # This file
└── .env                           # (Optional) API key file



