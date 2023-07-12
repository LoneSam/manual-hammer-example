
import requests
import json
from urllib.parse import quote
import time
import sys


headers = {
    'authority': 'play.flow.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.1.1402202574.1688224676; mp_776159d170484f49f19c3c2f7339f297_mixpanel=%7B%22distinct_id%22%3A%20%2218912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff%22%2C%22%24device_id%22%3A%20%2218912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Windows%22%2C%22%24browser%22%3A%20%22Chrome%22%2C%22%24browser_version%22%3A%20112%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22projectId%22%3A%20%229d23893a-95e7-4185-85f1-d5a7039463e5%22%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_GY6BHGBVKN=GS1.1.1688231612.2.0.1688231612.0.0.0',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
}



proxies = {
    "https": "http://127.0.0.1:8080",
}

for p in open(sys.argv[1],'r').readlines():
    p = p.replace('\n','')
    #cooked = cookie_part1 + quote(cook + p + cook2) + cookie_part2
    headers['cookie'] = '_ga=GA1.1.1402202574.1688224676; mp_776159d170484f49f19c3c2f7339f297'+p.replace('\u2026', '...')+'_mixpanel=%7B%22distinct_id%22%3A%20%2218912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff%22%2C%22%24device_id%22%3A%20%2218912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Windows%22%2C%22%24browser%22%3A%20%22Chrome%22%2C%22%24browser_version%22%3A%20112%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22projectId%22%3A%20%229d23893a-95e7-4185-85f1-d5a7039463e5%22%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_GY6BHGBVKN=GS1.1.1688231612.2.0.1688231612.0.0.0'
    start = time.time()
    response = requests.get("https://play.production.flow.com/query", headers=headers, proxies=proxies, verify='burp.pem')
    end = time.time()
    rtime = end - start
    rtime = round(rtime,3)
    print(response.status_code, len(response.headers), len(response.headers['Set-Cookie']), response.headers['Set-Cookie'], f"{rtime:.3f}", len(response.text), p.strip())
