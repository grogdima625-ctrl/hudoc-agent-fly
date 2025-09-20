import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_text_and_check(itemid):
    url = f"https://hudoc.echr.coe.int/eng#{itemid}"
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()
        if "Monaco" in text:
            print(f"✅ Найдено: {itemid}")
            return itemid
    except Exception as e:
        print(f"Ошибка: {itemid} — {e}")
    return None

def scan_range(start, end):
    found = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(get_text_and_check, f'001-{str(i).zfill(6)}') for i in range(start, end)]
        for future in as_completed(futures):
            result = future.result()
            if result:
                found.append(result)
    print(f"📊 Всего найдено дел по Monaco: {len(found)}")

scan_range(1, 1000)
