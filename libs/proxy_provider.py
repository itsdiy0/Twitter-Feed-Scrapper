import requests

def check_proxy(proxy):
    url = "http://www.example.com"
    proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"}

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False
    
def get_proxy():
    with open("proxies.txt","r") as proxies_file:
        proxies = proxies_file.read().splitlines()
        for proxy in proxies:
            if check_proxy(proxy):
                return proxy