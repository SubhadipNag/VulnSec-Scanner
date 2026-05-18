import requests

payloads = ["'", "\"", "' OR 1=1 --"]

errors = [
    "mysql",
    "sql syntax",
    "syntax error"
]

def scan_sqli(url):

    vulnerable = False

    for payload in payloads:

        test_url = f"{url}?id={payload}"

        response = requests.get(test_url)

        for error in errors:

            if error in response.text.lower():
                vulnerable = True

    return vulnerable
