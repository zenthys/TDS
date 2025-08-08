import time
import os
import random
import json, os
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import uiautomator2 as u2
import string

def color_256(code):
    return f'\033[38;5;{code}m'
color = {
    "pink": color_256(211),
    "rose": color_256(224),
    "vang": color_256(227),
    "lpink": color_256(174),
    "red": color_256(160),
    "1": color_256(146),
    "green": color_256(120),
    "cyan": color_256(51),
    "orange": color_256(208),
    "lime": color_256(154),
    "sky": color_256(117),
    "purple": color_256(129),
}
RESET = "\033[0m"
def generate_phpsessid(length=26):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
fake_session = generate_phpsessid()
ses = requests.Session()
config_file = "config.json"

try:
    config = json.load(open(config_file, "r", encoding="utf-8"))
    username = config["username"]
    password = config["password"]
    token = config["token"]
except:
    username = input(f'{color['green']}Nhập username: {color['rose']}').strip()
    password = input(f'{color['green']}Nhập password: {color['rose']}').strip()
    token = input(f'{color['green']}Nhập TDS Token: {color['rose']}').strip()

    json.dump(
        {"username": username, "password": password, "token": token},
        open(config_file, "w", encoding="utf-8"),
        indent=4,
        ensure_ascii=False
    )
cookies = {
    # 'cf_clearance': 'ZS0zJ3fEdJ1OMq1lmQkrVBebZMQAwsAg1OApimCi9p4-1754630039-1.2.1.1-bIBxrod4hqeEfm18BElRipqB5yGonRwGUbMF_Ray7bOon1_tMpgr5BgXyUl8881NNGIx2sOzRHevgb9eJ09jrDHSqegMaqnPUb8i.cFFlzSZORP4jvRhROOVpF6LBlMyCA3gPMo3EdfH2A.g_.dFO6FWHIWH0zSvclODGVB.aZLmiAD7D06_CE_98cHaMd8g2LrP_6ZjrYkDMlRodjySfVZqmson4r2vkl9E8KAcxXs',
    'PHPSESSID': fake_session,
}

headers_login = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://traodoisub.com',
    'priority': 'u=1, i',
    'referer': 'https://traodoisub.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"138.0.3351.121"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'cf_clearance=ZS0zJ3fEdJ1OMq1lmQkrVBebZMQAwsAg1OApimCi9p4-1754630039-1.2.1.1-bIBxrod4hqeEfm18BElRipqB5yGonRwGUbMF_Ray7bOon1_tMpgr5BgXyUl8881NNGIx2sOzRHevgb9eJ09jrDHSqegMaqnPUb8i.cFFlzSZORP4jvRhROOVpF6LBlMyCA3gPMo3EdfH2A.g_.dFO6FWHIWH0zSvclODGVB.aZLmiAD7D06_CE_98cHaMd8g2LrP_6ZjrYkDMlRodjySfVZqmson4r2vkl9E8KAcxXs; PHPSESSID=9696f3f0e911edcd2e6b923b1dddbff8',
}

data = {
    'username': username,
    'password': password,
}

response = ses.post('https://traodoisub.com/scr/login.php', cookies=cookies, headers=headers_login, data=data)

headers_id = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://traodoisub.com/home/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"138.0.3351.121"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.184", "Microsoft Edge";v="138.0.3351.121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
}

resid = ses.get('https://traodoisub.com/view/chtiktok/', cookies=cookies, headers=headers_id)
resid.encoding = "utf-8"

soup = BeautifulSoup(resid.text, "html.parser")

accounts = []

# Lấy dữ liệu: ID và Username
rows = soup.find_all("tr", class_="btn-reveal-trigger")
for row in rows:
    a_tag = row.find("a", href=lambda h: h and "tiktok.com" in h)
    tiktok_id = a_tag.text.strip() if a_tag else None
    
    span_tag = row.find("span", class_="badge-soft-success")
    username = span_tag.text.strip() if span_tag else None

    if tiktok_id and username:
        accounts.append({"id": tiktok_id, "username": username})

def acc_select():
    table = [[i + 1, acc["username"]] for i, acc in enumerate(accounts)]
    print(f'{color['rose']}')
    print(tabulate(table, headers=["STT", "TikTok ID"], tablefmt="rounded_grid", stralign="center", numalign="center"))
    RESET
    # Chọn account
    choice = int(input(f'{color['green']}Chọn tài khoản để chạy: {color['lpink']}'))
    if 1 <= choice <= len(accounts):
        tiktokid = accounts[choice - 1]["id"]
        print(f'{color['green']}Tài khoản đã chọn: {color['rose']}{accounts[choice - 1]['username']} {color['lpink']}(ID: {tiktokid})')
        params = {
            'fields': 'tiktok_run',
            'id': tiktokid,
            'access_token': token
        }
        response = ses.get(url,params=params).json()
        print(response['data']['msg'])
    else:
        print("Số bạn nhập không hợp lệ!")
    
url = "https://traodoisub.com/api/"
try:
    d = u2.connect()
except:
    print("Vui lòng kết nối điện thoại với máy tính")
    exit()


def countdown(time_1, time_2, message=f"{color['green']}ᴠᴜɪ ʟòɴɢ ᴄʜờ"):
    if time_1 > time_2:
        time_1, time_2 = time_2, time_1
    time_sec = random.randint(time_1, time_2)
    while time_sec >= 0:
        print(f'{message} {color["lpink"]}{time_sec:02d}s', end='\r')
        time.sleep(1)
        time_sec -= 1
def login():
    params = {
        'fields': 'profile',
        'access_token': token
    }

    res = ses.get(url,params=params).json()

    name = res['data']['user']
    xu = res['data']['xu']
    table_data = [
        ["User", name],
        ["Xu", xu]
    ]
    print(f'{color['rose']}')
    print(tabulate(table_data, tablefmt="rounded_grid", stralign="center", numalign="center"))
    RESET


def follow():
    total_job = 0
    while True:
        time.sleep(5)
        if total_job > 80:
            os.system(f'adb shell am force-stop com.ss.android.tt.creator >nul 2>&1')
            print(f'Đã dừng TikTok Studio')
            total_job = 0
            continue
        params = {
            'fields': 'tiktok_follow',
            'access_token': token
        }
        getjob = ses.get(url,params=params).json()
        if 'error' in getjob:
            countdown(getjob['countdown'],getjob['countdown'])
            continue
        else:
            donejob_url = 'https://traodoisub.com/api/coin/'
            if 'data' in getjob:
                for job in getjob['data']:
                    uid = job['real_id']
                    id = job['id']
                    os.system(f'adb shell am start -a android.intent.action.VIEW -d "snssdk567753://user/profile/{uid}" >nul 2>&1')
                    time.sleep(2)
                    follow_btn = d(className="android.widget.TextView", text="Follow")
                    if follow_btn.exists:
                        follow_btn.click()
                        countdown(8,12)
                        params_cpl = {
                            'type': 'TIKTOK_FOLLOW_CACHE',
                            'id': id,
                            'access_token': token
                        }
                        postjob = ses.get(donejob_url,params=params_cpl).json()
                        # print(postjob)
                        if 'cache' in postjob:
                            cache = postjob['cache']
                            msg = postjob['msg']
                            error = postjob['error']
                        else:
                            continue
                        if msg == 'Thành công':
                            print(f'{color['rose']}{msg} | {color['green']}https://tiktok.com/@{uid}')
                        else:
                            print(f'{color['red']}{error}')
                        if cache >= 8:
                            total_job += 8
                            params_coin = {
                                'type': 'TIKTOK_FOLLOW',
                                'id': 'TIKTOK_FOLLOW_API',
                                'access_token': token
                            }
                            time.sleep(3)
                            getcoin = ses.get(donejob_url,params=params_coin).json()
                            # print(getcoin)
                            if getcoin['success'] == 200:
                                mess = getcoin['data']['msg']
                                xu = getcoin['data']['xu']
                                xuthem = getcoin['data']['xu_them']
                                print(f'{color["green"]}{mess} | {color['lpink']}Xu hiện có: {xu}')
                                if xuthem < 5000:
                                    print(f'{color["red"]}Tài khoản TikTok bị nhả Follow')
                                    os.system('adb shell input keyevent 26')
                                    exit()
                            else:
                                er = getcoin['error']
                                print(er)
                                continue
            else:
                continue
def main():
    os.system('cls')
    login()
    acc_select()
    time.sleep(2)
    os.system('cls')
    print(f'{color['lpink']}TDS Follow TikTok')
    time.sleep(3)
    follow()
main()
