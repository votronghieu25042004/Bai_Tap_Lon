import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://batdongsan.com.vn/nha-dat-ban"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
cards = soup.find_all("div", class_="js__card")
links = []
for card in cards:
    a_tag = card.find("a", href=True)
    if a_tag:
        link = a_tag["href"]
        if not link.startswith("https://"):
            link = "https://batdongsan.com.vn" + link
        links.append(link)

print(f"Đã lấy được {len(links)} link bài viết.")

data = []
for link in links:
    print(f"Đang xử lý: {link}")
    try:
        res = requests.get(link, headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")

        title = soup.find("h1").text.strip()
        try:
            description = soup.find("div", class_="re__pr-short-description js__pr-description").text.strip()
        except:
            description = ""
        try:
            address = soup.find("div", class_="re__pr-short-address js__pr-address").text.strip()
        except:
            address = ""
        try:
            info_blocks = soup.find_all("span", class_="re__pr-specs-content-item")
            area = info_blocks[0].text.strip() if len(info_blocks) >= 1 else ""
            price = info_blocks[1].text.strip() if len(info_blocks) >= 2 else ""
        except:
            area = ""
            price = ""
        data.append([title, description, address, area, price])
    except Exception as e:
        print(f"Lỗi: {e}")
        continue

df = pd.DataFrame(data, columns=["Tiêu đề", "Mô tả", "Địa chỉ", "Diện tích", "Giá"])
df.to_excel("batdongsan_output.xlsx", index=False)
print(" Đã lưu file Excel: batdongsan_output.xlsx")
