from urllib.parse import urlparse, parse_qs

PAYLOADS = {
    "xss": "<script>alert('xss')</script>",
    "sqli": "' OR '1'='1",
    "ssrf": "http://localhost:8000"
}

INTERESTING_PATHS = ['admin', 'login', 'upload', 'debug']

def inject_payloads(path, p_type="xss"):
    parsed = urlparse(path)
    qs = parse_qs(parsed.query)
    new_qs = "&".join([f"{k}={PAYLOADS[p_type]}" for k in qs])
    return f"{parsed.path}?{new_qs}"

def is_interesting(path):
    return any(keyword in path.lower() for keyword in INTERESTING_PATHS)