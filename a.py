import requests
import re
import time
import random
import string
import json

ho_list = [
    "nguyen", "tran", "le", "pham", "hoang", "phan", "vu", "vo", "dang", "bui",
    "do", "ho", "ngo", "duong", "ly", "truong", "ha", "mai", "lai", "chau",
    "tan", "han", "huynh", "cao", "quach", "trinh", "ton", "ngan", "phung", "tang",
    "tieu", "ta", "mac", "la", "trieu", "phan", "hong", "hinh", "giang", "phat",
    "luu", "thach", "thoi", "tong", "dinh", "nghiem", "luong", "tan", "loc", "ky",
    "son", "tao", "trach", "nguy", "cam", "tien", "khuc", "nguyet", "kim", "bao",
    "quyen", "sam", "si", "phan", "thach", "lam", "mai", "khau", "nhan", "ngan",
    "luc", "khau", "thong", "nhiep", "ngoan", "thieu", "tuy", "nghi", "luu", "khong",
    "thi", "dieu", "tam", "hoac", "trac", "ngo", "dang", "trang", "huu", "khai",
    "dao", "dong", "ly", "nguyen", "nguyet", "dieu", "huynh", "thanh", "tu", "quynh"
]

ten_list = [
    "an", "binh", "chien", "duong", "hung", "khoa", "lam", "minh", "nam", "phuc",
    "quang", "son", "thanh", "viet", "xuan", "yen", "hai", "long", "ngoc", "trung",
    "tuan", "linh", "lan", "hanh", "mai", "huong", "nga", "thao", "anh", "chi",
    "giang", "dao", "ly", "ha", "loan", "nhan", "tam", "dao", "thu", "uyen",
    "tien", "quynh", "hoa", "oanh", "khanh", "duyen", "anhthu", "thuy", "nhu", "my",
    "phuong", "cam", "vy", "daoanh", "bich", "hong", "lananh", "kieu", "thuong", "ngan",
    "toan", "phat", "trinh", "loc", "hieu", "dang", "bao", "sonlam", "quoc", "tai",
    "tri", "phuoc", "vuong", "nghia", "thuong", "kien", "luan", "kiet", "truong", "thien",
    "quocbao", "minhquan", "giap", "hungmanh", "thinh", "duy", "tinh", "vinh", "hoan", "lap",
    "thang", "phong", "khanhduy", "tung", "hieu", "cuong", "dung", "vietanh", "thienan", "anhkhoa"
]

domains = [
    "@donglucsport.com",
    "@quanlytinhgon.vn",
    "@satato.com.vn",
    "@batdongsanvgp.com",
    "@mail.hunght1890.com",
    "@hoanganh.mx",
    "@lienvietlaw.com",
    "@toanthinhphatmedical.com",
    "@inpos.com.vn",
    "@itemjunction.net",

]

def random_username():
    ho = random.choice(ho_list)
    ten = random.choice(ten_list)
    # random 2-3 chữ cái
    letters = ''.join(random.choices(string.ascii_letters, k=random.randint(2, 3)))
    # random số từ 1000 đến 99999
    number = str(random.randint(1000, 99999))
    suffix = letters + number
    return ho + ten + suffix
# def random_username():
#     ho = random.choice(ho_list)
#     ten = random.choice(ten_list)
#     suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
#     return ho + ten + suffix

def create_temp_mail():
    username = random_username()
    domain = random.choice(domains)
    return username + domain
def send_otp(username,mail):
    cookies = {
        '_ga': 'GA1.1.1670241420.1757043722',
        '_ga_1M7M9L6VPX': 'GS2.1.s1757054158$o3$g1$t1757054164$j54$l0$h0',
        'datadome': 'ywuw_ll~Jjo0amQqF1w3Q3N6gS6enb~oKuUcpvodEHwjQoIc_GAG0CyqiC2xaLq5eNj5R5HleEyHW3JGmiTdyNQ1SOxSt3pVFJYfVWaQ3JbyxMjXde5NAIiNCZP9UNQM',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'https://sso.garena.com',
        'Referer': 'https://sso.garena.com/universal/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': '_ga=GA1.1.1670241420.1757043722; _ga_1M7M9L6VPX=GS2.1.s1757054158$o3$g1$t1757054164$j54$l0$h0; datadome=y3_0IoncH~C~shBTaxoCwk0FRnDysnQPMW~r9ztuASZvDTQLJttrPS~4XBbTKws8lrcl69KFRwGuPlCGUAG_UriT69n6twFPhfu_n~ZkyFHVJDTFhAssOTGkhCUZtTRm',
    }

    data = {
        'username': username,
        'email': mail,
        'locale': 'vi-VN',
        'format': 'json',
        'id': int(time.time() * 1002),
    }

    try:
        response = requests.post('https://sso.garena.com/api/send_register_code_email', cookies=cookies, headers=headers, data=data)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("result") == 0:
                print("Gửi OTP thành công")
                return True
            else:
                
                return False

        else:
            
            return False
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {e}")
        return False
def get_code(mail):
    i = 0
    while True:
        if i>=10:
            print("Không thể lấy mã, hãy tạo tài khoản khác dưới đây")
            return False
        try:
            data = requests.get(f'https://hunght1890.com/{mail}').text
            otp_match = re.search(r"\*\*(\d+)\*\*", data)
            if otp_match:
                print(f"Lấy thành công OTP {otp_match.group(1)}")
                return otp_match.group(1)
            else:
                continue
        except:
            i+=1
            time.sleep(3)
            continue
def reg(username,code,mail):
    cookies = {
        '_ga': 'GA1.1.1670241420.1757043722',
        '_ga_1M7M9L6VPX': 'GS2.1.s1757054158$o3$g1$t1757054164$j54$l0$h0',
        'datadome': 'ywuw_ll~Jjo0amQqF1w3Q3N6gS6enb~oKuUcpvodEHwjQoIc_GAG0CyqiC2xaLq5eNj5R5HleEyHW3JGmiTdyNQ1SOxSt3pVFJYfVWaQ3JbyxMjXde5NAIiNCZP9UNQM',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'https://sso.garena.com',
        'Referer': 'https://sso.garena.com/universal/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'username': username,
        'email': mail,
        'email_otp': code,
        'password': '4ecdfe7ff3ea0d7726e703765ae26a52d2aef984bd95de0ccb389d74dcffabfec4a7cb0f650b81f51b493c9189997bedd02f47b8ce0608ebc88688c9f889229eb9266bde30e398e62427dc796d8b98081834b77eecfbc32222ad5a9c60f2f18910a675b24a7201da4cc023925e176b3f1f44f18cb4654a951561f4b8aaa73add',
        'location': 'VN',
        'locale': 'vi-VN',
        'format': 'json',
        'id': int(time.time() * 1002),
    }

    response = requests.post('https://sso.garena.com/api/register', cookies=cookies, headers=headers, data=data)
    if response.status_code == 200:
        if 'username' in response.json():
            password = "Kocopass11@#"
            with open("accounts.txt", "a", encoding="utf-8") as f:
                f.write(f"{username} | {password}\n")
            return True
        else:
            return False
    else:
        return False


def main():
    check = requests.get('https://raw.githubusercontent.com/zenthys/TDS/refs/heads/main/check.json').text
    if 'online' in check:
        try:
            n = int(input("Nhập số tài khoản muốn tạo: "))
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")
            return
        d = 0
        while True:
            if d==n:
                print(f"Đã reg xong {d} acc")
                return
            try:
                username = random_username()
                mail = create_temp_mail()
                print(mail)
            except Exception as e:
                print("Lỗi khi tạo username")
                continue
            try:
                send_otp(username=username,mail=mail)
                time.sleep(10)
            except Exception as e:
                print("Lỗi khi gửi OTP")
                continue

            try:
                code = get_code(mail=mail)
                time.sleep(10)
            except Exception as e:
                print("Lỗi khi lấy mã",e)
                continue

            if reg(username=username, code=code,mail=mail):
                password = "Kocopass11@#"
                d+=1
                print(f"[{d}] {username} | {password} | Success")
                time.sleep(5)
            else:
                print(f"{username} | {password} | Failed")
    else:
        print("Lỗi không xác định!")
        exit()
main()

