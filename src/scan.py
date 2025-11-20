#!/usr/bin/env python3
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

def scan_port(host: str, port: int, timeout=0.8) -> dict:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        res = s.connect_ex((host, port))
        if res == 0:
            banner = ''
            try:
                s.sendall(b"\n")
                banner = s.recv(1024).decode(errors='ignore').strip()
            except Exception:
                banner = ''
            s.close()
            return {'port': port, 'open': True, 'banner': banner}
        s.close()
    except Exception:
        pass
    return {'port': port, 'open': False, 'banner': ''}

def scan_range(host: str, start: int, end: int, workers: int = 200):
    ports = range(start, end+1)
    results = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(scan_port, host, p): p for p in ports}
        for fut in as_completed(futures):
            res = fut.result()
            if res:
                results.append(res)
    return sorted(results, key=lambda x: x['port'])

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python scan.py <host> <start_port> <end_port>')
        sys.exit(1)
    host = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    res = scan_range(host, start, end)
    for r in res:
        if r['open']:
            print(f"Port {r['port']} OPEN - Banner: {r['banner']}")
