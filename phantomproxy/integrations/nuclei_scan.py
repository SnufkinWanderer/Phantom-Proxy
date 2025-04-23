import subprocess

def scan_with_nuclei(target_url):
    print(f"[Nuclei] Scanning: {target_url}")
    result = subprocess.run(["nuclei", "-u", target_url], capture_output=True, text=True)
    return result.stdout