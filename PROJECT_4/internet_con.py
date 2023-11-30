import requests

def check_internet():
    url = 'http://www.google.com/'
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("Internet connection not available")
    return False
if check_internet():
    print("You are connected to the internet")
else:
    print("You are not connected to the internet")

