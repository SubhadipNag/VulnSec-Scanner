import requests

payload = "<script>alert('xss')</script>"

def scan_xss(url):

    test_url = f"{url}?q={payload}"

    response = requests.get(test_url)

    return payload in response.text
