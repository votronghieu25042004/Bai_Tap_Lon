# Bai_Tap_Lon
# Web Scraping Bất Động Sản từ Batdongsan.com.vn

Script Python tự động thu thập dữ liệu bài đăng bất động sản từ [batdongsan.com.vn](https://batdongsan.com.vn) và lưu thông tin vào file Excel. Có thể thiết lập lịch chạy mỗi ngày lúc 06:00 sáng.
---
##  Tính năng
- Tự động thu thập dữ liệu từ trang **batdongsan.com.vn**
- Lấy thông tin chi tiết:
  - Tiêu đề bài đăng
  - Mô tả chi tiết
  - Địa chỉ
  - Diện tích
  - Giá
- Lưu dữ liệu vào file Excel (`batdongsan_output.xlsx`)
- Thiết lập chạy tự động mỗi ngày vào 06:00 sáng
- Xử lý lỗi khi thiếu thông tin hoặc không tải được dữ liệu
##  Yêu cầu cài đặt
- Python 3.x
- Thư viện Python:
  - `selenium==4.18.1`
  - `pandas==2.2.1`
  - `schedule==1.2.1`
  - `webdriver-manager==4.0.1`
  - `openpyxl==3.1.2`

Cài đặt nhanh bằng lệnh:
```bash
pip install -r requirements.txt
Hướng dẫn cài đặt WebDriver
Kiểm tra phiên bản Chrome đang dùng:
Mở Chrome → Nhập chrome://version

Tải ChromeDriver tương ứng tại:
https://sites.google.com/chromium.org/driver/

Giải nén và:

Đặt chromedriver.exe vào cùng thư mục với file script
hoặc

Thêm đường dẫn đến chromedriver.exe vào biến môi trường PATH

Cách sử dụng với Visual Studio Code
Mở VS Code và tạo file main.py

Dán mã Python vào file

Mở Terminal trong VS Code (nhấn Ctrl + ~)

Cài thư viện:

bash
Sao chép
Chỉnh sửa
pip install selenium pandas schedule openpyxl webdriver-manager
Chạy script:

bash
Sao chép
Chỉnh sửa
python main.py
Cấu trúc dữ liệu đầu ra
File Excel: batdongsan_output.xlsx
Gồm các cột:

Tiêu đề	Mô tả	Địa chỉ	Diện tích	Giá

Lên lịch tự động
Script dùng thư viện schedule để chạy hằng ngày lúc 06:00:

python
Sao chép
Chỉnh sửa
schedule.every().day.at("06:00").do(fetch_data)