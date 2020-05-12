import requests
import time
import string


url = '' #put in a WP-like API endpoint

proxylist = open("list.txt", "r") #list txt is a proxy list
i=0
payload ={'action':'wp_ulike_process','id':'x','nonce': 'x', 'type': 'likeThis', 'template': 'x'} #object to send to API, you can find it using developer console in Google Chrome

for proxy in proxylist:
    i=i+1
    print(i)
    try:
        k= "https://"+proxy
        x = requests.post(url, data = payload,proxies={"https": k},timeout=7)
    except (requests.ConnectionError,
                requests.RequestException,
                requests.TooManyRedirects,
                requests.RequestException):
        continue
    
    if(x.text.find('status":2')!=-1):
        try:
            k= "https://"+proxy
            x = requests.post(url, data = payload,proxies={"https": k},timeout=7)
        except (requests.ConnectionError,
                requests.RequestException,
                requests.TooManyRedirects,
                requests.RequestException):
            continue
print('LIST DONE')