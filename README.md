# 🔍 DNS Lookup Tool (Python)

A simple and colorful **DNS record lookup utility** built with Python.  
This script uses [`dnspython`](https://www.dnspython.org/) for DNS resolution and [`rich`](https://github.com/Textualize/rich) for beautiful console output.

---

## 🚀 Features

✅ Fetches multiple DNS record types at once:
- `A`
- `AAAA`
- `MX`
- `NS`
- `SOA`
- `TXT`
- `CNAME`

✅ Handles timeouts and errors gracefully  
✅ Colorful, well-formatted output using the **Rich** library  
✅ Works cross-platform (Windows, macOS, Linux)

---

## 🧩 Example Output

```bash
Enter a domain name (e.g., example.com): yahoo.com
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Record Type  ┃ Value                                ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ A            │ 74.6.231.20                          │
│ AAAA         │ 2001:4998:44:3507::8001              │
│ MX           │ 1 mta6.am0.yahoodns.net.             │
│ ...          │ ...                                  │
└──────────────┴──────────────────────────────────────┘

```

## 📸 Screenshots

<img width="1917" height="914" alt="image" src="https://github.com/user-attachments/assets/3a3df02a-29ec-45a2-bd2a-8a2ca7855b1e" />
