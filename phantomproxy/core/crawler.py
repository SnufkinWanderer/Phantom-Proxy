import requests
from bs4 import BeautifulSoup
from .payloads import PAYLOADS

def crawl_and_inject(url, payload_type="xss"):
    visited = set()
    to_visit = [url]
    while to_visit:
        current = to_visit.pop()
        if current in visited:
            continue
        visited.add(current)
        try:
            res = requests.get(current, timeout=3)
            soup = BeautifulSoup(res.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                target = link['href']
                if '?' in target:
                    injected = target.split('?')[0] + '?injected=' + PAYLOADS[payload_type]
                    print(f"[Crawler] Injecting: {injected}")
                    requests.get(injected)
                elif target.startswith('http') and target not in visited:
                    to_visit.append(target)
        except:
            continue