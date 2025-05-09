from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import schedule

def fetch_data():
    # 1. Vào website đã chọn
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    url = "https://batdongsan.com.vn/nha-dat-ban"
    driver.get(url)

    # 2. Click chọn bất kỳ Tỉnh/TP (Hà Nội, Đà Nẵng, Hồ Chí Minh, ...) và ngành nghề (nếu có)
    #  Em Bỏ qua bước này do trang batdongsan.com.vn không yêu cầu chọn ngành nghề cụ thể và không có ô tìm kiếm như các trang tuyển dụng.

    # 3. Bấm tìm kiếm (nếu có Button tìm kiếm)
    #  Em Bỏ qua bước này vì không cần thực hiện tìm kiếm trên trang này, dữ liệu được hiển thị sẵn.

    try:
        # 4. Đợi trang tải xong các bài đăng
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js__card"))
        )
    except:
        print("Không tìm thấy bài đăng.")
        driver.quit()
        return

    # 5. Lấy tất cả dữ liệu của các trang.
    cards = driver.find_elements(By.CLASS_NAME, "js__card")
    print(f"Số bài viết tìm thấy: {len(cards)}")

    data = []

    # 6. Lấy tất cả dữ liệu (Tiêu đề, Mô tả, Hình ảnh, Nội dung bài viết) hiển thị ở bài viết.
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
    # 7. Lưu dữ liệu đã lấy được vào file Excel hoặc CSV.
    df = pd.DataFrame(data, columns=["Tiêu đề", "Mô tả", "Địa chỉ", "Diện tích", "Giá"])
    df.to_excel("batdongsan_output.xlsx", index=False)
    print("Đã lưu file Excel: batdongsan_output.xlsx")

# 8. Set lịch chạy vào lúc 6h sáng hàng ngày
schedule.every().day.at("06:00").do(fetch_data)

while True:
    schedule.run_pending()
    time.sleep(60)
# fetch_data() chạy luôn không cần chờ đến 06:00
# 9. Tạo project Github chế độ public.
# 10. Viết file README.md hướng dẫn cài đặt cho project Github đầy đủ rõ ràng.
# 11. Push (file code, README.md, requirements.txt) lên project và nộp link project Github vào classroom.
