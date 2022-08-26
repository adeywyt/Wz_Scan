import sys
import requests
import time
from colorama import init
init(autoreset=True)
own = r'''
 __      __           _________                     
/  \    /  \________ /   _____/ ____ _____    ____  
\   \/\/   /\___   / \_____  \_/ ___\\__  \  /    \ 
 \        /  /    /  /        \  \___ / __ \|   |  \
  \__/\__/  /______\/_________/\_____>______/___|__/
                作者:forget    v1.1
使用：
[+]python Wz_Scan.py https url
[+]python Wz_Scan.py http  url
'''
try:
    http = sys.argv[1]
    url = sys.argv[2]
    wfile = open("子域名收集.txt", "w")
except:
    print(own)
    sys.exit(1)
print(own)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}
start = time.time()
print("扫描开始(扫描时间比较久):")
with open("dic.txt", "r") as txt:
    for wz in txt.readlines():
        wz = wz.strip()
        newurl = http + "://" + wz + "." + url
        try:
            response = requests.get(newurl, headers=headers)
        except:
            print("[-]", newurl)
            continue
        code = response.status_code
        if code == 200:
            print("\033[0;32;40m[+]子域名存在：%s\033[0m" % newurl)
            wfile.write(newurl)
    endtime = time.time()
    uestime = start - endtime
    print("所用时间：%s" % uestime)
