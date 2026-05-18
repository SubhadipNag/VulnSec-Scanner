import requests

directories = [
    "admin",
    "login",
    "backup",
    "uploads"
]

def scan_directories(url):

    found = []

    for directory in directories:

        target = f"{url}/{directory}"

        response = requests.get(target)

        if response.status_code == 200:
            found.append(target)

    return found
