from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import schedule

def fetch_data():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    url = "https://batdongsan.com.vn/nha-dat-ban"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js__card"))
        )
    except:
        print("⛔ Không tìm thấy bài đăng.")
        driver.quit()
        return

    cards = driver.find_elements(By.CLASS_NAME, "js__card")
    print(f"✅ Số bài viết tìm thấy: {len(cards)}")

    data = []

    #  Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Hình ảnh, Nội dung bài viết) hiển thị ở bài viết.
    for card in cards:
        try:
            title = card.find_element(By.TAG_NAME, "h3").text  # Tiêu đề bài viết
        except:
            title = ""
        try:
            description = card.find_element(By.CLASS_NAME, "re__card-description").text  # Mô tả 
        except:
            description = ""
        try:
            address = card.find_element(By.CLASS_NAME, "re__card-location").text  # Địa chỉ
        except:
            address = ""
        try:
            specs = card.find_elements(By.CLASS_NAME, "re__card-config-item")  # Diện tích và giá
            area = specs[0].text if len(specs) > 0 else ""
            price = specs[1].text if len(specs) > 1 else ""
        except:
            area = ""
            price = ""

        item = [title, description, address, area, price]
        data.append(item)

    driver.quit()

    # Lưu dữ liệu đã lấy được vào file excel hoặc csv.
    df = pd.DataFrame(data, columns=["Tiêu đề", "Mô tả", "Địa chỉ", "Diện tích", "Giá"])
    df.to_excel("batdongsan_output.xlsx", index=False)
    print("✅ Đã lưu file Excel: batdongsan_output.xlsx")

# Set lịch chạy vào lúc 6h sáng hằng ngày.
schedule.every().day.at("06:00").do(fetch_data)  
while True:
    schedule.run_pending()
    time.sleep(60)
