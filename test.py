import json

import requests

def getPhoneDetails(number):

    url='https://www.truecaller.com/api/search?type=4&countryCode=in&q='+number

    header={
        'authorization': 'Bearer pS-iaJAgya6ng9wr5kB_tFfwY3r2-UHR',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://www.truecaller.com/search/in/8527326325',
    'authority': 'www.truecaller.com',
    'cookie': '__cfduid=d24db64dda3e55355e61aa19fb96d43861512806307; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; _ga=GA1.2.39977844.1512805092; _gid=GA1.2.1116580210.1512805092; XLBS3=XLBS2|Wiup+|WiuXp'
    }

    r=requests.get(url=url,headers=header)
    print(r.text)
    js=json.loads(r.text)["data"][0]
    print(js["name"])
    print(js["gender"])
    print(js["addresses"][0]['area'])
    print(js["internetAddresses"][0]["id"])


n=input()
getPhoneDetails(n)