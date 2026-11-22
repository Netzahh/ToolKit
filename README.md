# 🛡️ Network Security Tool

A simple Python command-line toolkit for network information, IP/CIDR calculation and port scanning.

Built with the Python standard library only, so there is nothing to install.

---

## ✨ Features

| Option | Description |

| **System Information** | Shows the current user, date, Python version and machine name |
| **Network Information** | Displays hostname, local IP, destination IP and port, and saves the results to a file |
| **Ip Calculator** | Computes the subnet mask, total addresses and usable hosts from an IP address and a CIDR |
| **Local Port Scan** | Scans a target (IP or hostname) for open ports between 80 and 444 |
| **View Result** | Re-runs the network info or displays the previously saved results |

---

## 📦 Requirements

- Python 3.x
- No external libraries (only `socket`, `sys`, `os` and `datetime`)

---

## 🚀 Installation

```bash
git clone https://github.com/Netzahh/ToolKit.git
cd ToolKit
```

## ▶️ Usage

Linux / macOS:

```bash
python3 ToolKit.py
```

Windows:

```bash
python ToolKit.py
```



## 💾 Saved results

The **Network Information** option appends its results to a file named `Scan_Result`, created in the folder where you run the script. Use **View Result** to read it back.

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and for use on machines and networks that **you own or have explicit permission to test**. Scanning systems without authorization may be illegal. The author is not responsible for any misuse.

## 👤 Author

**Netzahh** — [GitHub](https://github.com/Netzahh)
