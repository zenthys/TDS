import time
import os
import random
import json, os
import requests
import uiautomator2 as u2

ses = requests.Session()
try:
    token = json.load(open("config.json"))["token"]
except:
    token = input("Nhập TDS Token: ").strip()
    json.dump({"token": token}, open("config.json", "w"))

# token = 'TDS9JSOyVmdlNnI6IiclZXZzJCLi8mcQ9mTxEDRiojIyV2c1Jye'
url = "https://traodoisub.com/api/"
try:
    d = u2.connect()
except:
    print("Vui lòng kết nối điện thoại với máy tính")
    exit()

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
def fakehuman(so_video=7, delay_range=(20, 22)):
    for i in range(so_video):
        try:
            d.swipe(0.5, 0.8, 0.5, 0.2, duration=0.05)
            rd = random.randint(1, 10)
            delay = random.uniform(*delay_range)
            print(f"[{i+1}]⏳ Xem video {delay:.1f} giây...")
            time.sleep(delay)
            if rd == 1:
                print(f'Action: Tym')
                bt = d.xpath('//android.widget.Button[contains(@content-desc, "Thích video.")]')
                if bt.exists:
                    bt.click()

            elif rd == 2:
                print(f'Action: Favorite')
                bt = d.xpath('//android.widget.Button[contains(@content-desc, "Thêm hoặc xóa video này khỏi mục Yêu thích.")]')
                if bt.exists:
                    bt.click()

            elif rd == 3 or rd == 5:
                print(f'Action: Đăng lại')
                bt = d.xpath('//android.widget.Button[contains(@content-desc, "Chia sẻ video.")]')
                if bt.exists:
                    bt.click()
                    time.sleep(0.6)
                    if d(text="Đăng lại").exists:
                        d(text="Đăng lại").click()
                    else:
                        if d(text="Sao chép Liên kết").exists:
                            d(text="Sao chép Liên kết").click()
                        else:
                            width, height = d.window_size()
                            x = width // 2
                            y = height // 2
                            d.click(x, y)
        except:
            print("Vui lòng kết nối điện thoại với máy tính")
            exit()
    print("✅ Done.")

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
    print(f'{color["green"]}User: {color["rose"]}{name}')
    print(f'{color["green"]}Xu: {color["rose"]}{xu}')

    tiktokid = input(f'{color["green"]}Nhập id tiktok cần chạy: ')
    params = {
        'fields': 'tiktok_run',
        'id': tiktokid,
        'access_token': token
    }

    response = ses.get(url,params=params).json()
    print(response['data']['msg'])

def follow():
    job_error = 0
    while True:
        time.sleep(5)
        if job_error >= 3:
            print("Acc TikTok bị nhả follow hoặc đã xảy ra lỗi")
            exit()
        params = {
            'fields': 'tiktok_follow',
            'access_token': token
        }
        getjob = ses.get(url,params=params).json()
        if 'error' in getjob:
            countdown(getjob['countdown'])
            time.sleep(1)
            getjob = ses.get(url,params=params).json()
        else:
            donejob_url = 'https://traodoisub.com/api/coin/'
            for job in getjob['data']:
                uid = job['real_id']
                id = job['id']
                os.system(f'adb shell am start -a android.intent.action.VIEW -d "snssdk567753://user/profile/{uid}" >nul 2>&1')
                time.sleep(3)
                follow_btn = d(className="android.widget.TextView", text="Follow")
                if follow_btn.exists:
                    follow_btn.click()
                    countdown(15,20)
                    params_cpl = {
                        'type': 'TIKTOK_FOLLOW_CACHE',
                        'id': id,
                        'access_token': token
                    }
                    postjob = ses.get(donejob_url,params=params_cpl).json()
                    cache = postjob['cache']
                    msg = postjob['msg']
                    error = postjob['error']
                    if msg == 'Thành công':
                        print(f'{color['rose']}{msg} | {id}')
                        job_error = 0
                    else:
                        print(f'{color['red']}{error}')
                        job_error += 1
                    if cache >= 8:
                        params_coin = {
                            'type': 'TIKTOK_FOLLOW',
                            'id': 'TIKTOK_FOLLOW_API',
                            'access_token': token
                        }
                        time.sleep(3)
                        getcoin = ses.get(donejob_url,params=params_coin).json()
                        if getcoin['success'] == 200:
                            mess = getcoin['data']['msg']
                            xu = getcoin['data']['xu']
                            print(f'{color["green"]}{mess} | {color['lpink']}Xu hiện có: {xu}')
                        else:
                            er = getcoin['error']
                            print(er)
                        # print(f'{color["green"]}Lướt video chống nhả follow')
                        # os.system(f'adb shell am start -a android.intent.action.VIEW -d "snssdk1233://aweme/detail/" >nul 2>&1')
                        # fakehuman()

def main():
    login()
    print(f'{color['lpink']}TDS Follow TikTok')
    time.sleep(3)
    follow()
main()
#adb connect 192.168.1.146:5555
