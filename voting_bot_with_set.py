import requests
import random

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

vote_count = 0
proxy_set = set()
success_message = '{"success":true,"code":"0","msg":null,"data":{"result":"success","extra":null}}'
proxy_file = open(r"C:\socks4.txt", "r") # ip:port
proxy_set.update(proxy_file.readlines())
proxy_file.close()

while True:
    proxy = random.choice(list(proxy_set))
    proxyDict = {
        "https": "socks4://" + proxy
    }

    try:
        with requests.Session() as session:
            url = "https://www.site.com/vote"
            request = session.post(url, headers=headers, proxies=proxyDict, timeout=1)
            if request.text == success_message:
                vote_count = vote_count + 1
                print("voted times: %s" % vote_count)
                print("good proxy: %s" % proxy)
            else:
                print("already voted")
    except:
        print("Proxy Connection Error: %s" % proxy)