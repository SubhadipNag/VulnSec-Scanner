import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security"
]

def analyze_headers(url):

    findings = []

    response = requests.get(url)

    for header in SECURITY_HEADERS:

        if header not in response.headers:
            findings.append(f"{header} missing")

    return findings
