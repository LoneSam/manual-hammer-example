#https://open.spotify.com/track/0UQOPPZrDqzn2AxnOTX2Hl?si=52866fabddad418d
import requests
import json
from urllib.parse import quote
import time
import sys

method = "POST"
url = "/query"
http_version = "HTTP/2"
host = "play.production.REDACTED.com"
cookie_part1 = "autoincrement=1688224674.802.35.868226"
cookie_part11 = "|95b0577dfc07a775a78ddf94f79bfdab; _ga=GA1.1.1402202574.1688224676; mp_776159d170484f49f19c3c2f7339f297_mixpanel="
#cookie_sandwich = "%7B%22distinct_id%22%3A%20%2218912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff%22%2C%22%24device_id%22%3A%20%2218912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Windows%22%2C%22%24browser%22%3A%20%22Chrome%22%2C%22%24browser_version%22%3A%20112%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22projectId%22%3A%20%229d23893a-95e7-4185-85f1-d5a7039463e5%22%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D"
cook = """{"distinct_id": "18912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff","$device_id": "18912082a9a9ca-09b1eedf2e371d-1736307c-1d73c0-18912082a9c1fff","$initial_referrer": "$direct","$initial_referring_domain": "$direct","__mps": {"$os": "Windows","$browser": "Chrome","$browser_version": 112,"$initial_referrer": "$direct","$initial_referring_domain": "$direct","projectId": "9d23893a-95e7-4185-85f1-d5a7039463e5"},"__mpso": {},"__mpus": {},"__mpa": {},"__mpu": {},"__mpr": [],"__mpap": []}"""
cookie_part2 = "; REDACTED-playground=MTY4ODIyNDc4NXxEdi1CQkFFQ180SUFBUkFCRUFBQVJQLUNBQUVHYzNSeWFXNW5EQWdBQm5WelpYSkpSQVp6ZEhKcGJtY01KZ0FrWm1VNE16WXlZVEl0WkRVeVlpMDBaRFF5TFRobU9XTXRZak13TXpka09EYzNOR016fEK0L9HSvU8e39egQB1DJPJUOq8sfeCJPEQvKbPEsT-o; _ga_GY6BHGBVKN=GS1.1.1688224676.1.1.1688224785.0.0.0"
content_length = "951"
sec_ch_ua = "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\""
accept = "*/*"
content_type = "application/json"
sec_ch_ua_mobile = "?0"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36"
sec_ch_ua_platform = "\"macOS\""
origin = "https://play.REDACTED.com"
sec_fetch_site = "same-site"
sec_fetch_mode = "cors"
sec_fetch_dest = "empty"
referer = "https://play.REDACTED.com/"
accept_encoding = "gzip, deflate"
accept_language = "en-US,en;q=0.9"

body = {
    "operationName": "GetProject",
    "variables": {"projectId": "9d23893a-95e7-4185-85f1-d5a7039463e5"},
    "query": "query GetProject($projectId: UUID!) {\n  project(id: $projectId) {\n    id\n    persist\n    mutable\n    parentId\n    updatedAt\n    seed\n    title\n    description\n    readme\n    accounts {\n      address\n      deployedContracts\n      state\n      __typename\n    }\n    contractTemplates {\n      id\n      script\n      title\n      index\n      __typename\n    }\n    transactionTemplates {\n      id\n      script\n      title\n      index\n      __typename\n    }\n    scriptTemplates {\n      id\n      script\n      title\n      index\n      __typename\n    }\n    contractDeployments {\n      id\n      script\n      title\n      address\n      blockHeight\n      __typename\n    }\n    transactionExecutions {\n      id\n      script\n      arguments\n      signers\n      logs\n      __typename\n    }\n    __typename\n  }\n}\n"
}


headers = {
    "Host": host,
    "Cookie": cookie_part1 + cookie_part11 + quote(cook) + cookie_part2,
    "Content-Length": content_length,
    "Sec-Ch-Ua": sec_ch_ua,
    "Accept": accept,
    "Content-Type": content_type,
    "Sec-Ch-Ua-Mobile": sec_ch_ua_mobile,
    "User-Agent": user_agent,
    "Sec-Ch-Ua-Platform": sec_ch_ua_platform,
    "Origin": origin,
    "Sec-Fetch-Site": sec_fetch_site,
    "Sec-Fetch-Mode": sec_fetch_mode,
    "Sec-Fetch-Dest": sec_fetch_dest,
    "Referer": referer,
    "Accept-Encoding": accept_encoding,
    "Accept-Language": accept_language
}


proxies = {
    "https": "http://127.0.0.1:8080",
}

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

for p in open(sys.argv[1],'r').readlines():
    p = p.replace('\n','')
    #cooked = cookie_part1 + quote(cook + p + cook2) + cookie_part2
    headers['cookie'] = cookie_part1 + p.replace('\u2026', '...') + cookie_part11 + quote(cook) + cookie_part2
    start = time.time()
    response = requests.post("https://play.production.REDACTED.com/query", headers=headers, data=json.dumps(body), proxies=proxies, verify='burp.pem')
    end = time.time()
    rtime = end - start
    rtime = round(rtime,3)
    print(response.status_code, len(response.headers), f"{rtime:.3f}", len(response.text), p.strip())
