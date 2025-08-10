<h1 align="center">🔍 Port Scanner</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge">
  <br>
  <img src="https://img.shields.io/badge/Author-ROSHAN--Z89-green?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>

---

## 🧠 Description

**Port Scanner** is a lightweight multi-threaded TCP/UDP port scanner written in Python. It scans a target host over a given port range and reports open ports. Built for educational purposes and penetration testing scenarios.

> ⚠️ **Disclaimer:** This tool is for educational and ethical hacking purposes only. Do **not** use it without proper authorization.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| ⚡ Multi-threaded Scanning | Uses Python's `threading` to speed up scanning. |
| 🌍 Target Hostname Resolution | Automatically resolves domain names to IPs. |
| 🔌 TCP & UDP Support | Checks both TCP and UDP ports (basic UDP check). |
| 📜 Custom Port Range | Choose your own start and end ports. |
| 🪶 Lightweight | Pure Python with no heavy dependencies. |
| 📦 Cross-Platform | Runs on Windows, Linux, and Mac. |

---

## 📦 Installation

🧪 Works best on Python 3.8 or above

```bash
git clone https://github.com/ROSHAN-Z89/python-port-scanner
cd python-port-scanner
python3 port_scanner.py <TARGET> <START_PORT> <END_PORT>
