# mini-nmap
The aim of this project is to build a simple Python-based tool that can scan a target system for open ports, similar to how Nmap performs basic scanning. This project helps you understand how network connections, ports, and TCP handshakes work.

# mini-nmap (starter)
Concurrent TCP port scanner. Usage (example):

```bash
python src/scan.py 127.0.0.1 20 1024
```

This will scan ports 20..1024 on 127.0.0.1 and print open ports and (when possible) a simple banner.

**Ethics:** Only scan hosts you own or have explicit permission to test.
