# Bai_Tap_Lon  
## Web Scraping Bất Động Sản từ Batdongsan.com.vn

Script Python tự động thu thập dữ liệu bài đăng bất động sản từ [batdongsan.com.vn](https://batdongsan.com.vn) và lưu thông tin vào file Excel. Có thể thiết lập lịch chạy mỗi ngày lúc **06:00 sáng**.

---

##  Tính năng

- Tự động thu thập dữ liệu từ trang **batdongsan.com.vn**
- Lấy thông tin chi tiết bài đăng:
  - Tiêu đề
  - Mô tả
  - Địa chỉ
  - Diện tích
  - Giá
- Lưu dữ liệu vào file Excel: `batdongsan_output.xlsx`
- Thiết lập chạy tự động mỗi ngày lúc **06:00**
- Xử lý lỗi khi thiếu thông tin hoặc không tải được dữ liệu

---

##  Yêu cầu cài đặt

- Python 3.x
- Các thư viện Python:

```bash
pip install -r requirements.txt
Hoặc cài trực tiếp:
- bash
- Sao chép
- Chỉnh sửa
pip install selenium pandas schedule openpyxl webdriver-manager
Hướng dẫn cài đặt ChromeDriver
Kiểm tra phiên bản Chrome bạn đang sử dụng:
Mở trình duyệt và nhập chrome://version

Tải ChromeDriver tương ứng tại:
https://sites.google.com/chromium.org/driver/

Cách sử dụng:
Đặt chromedriver.exe cùng thư mục với file Python
Thêm đường dẫn chromedriver.exe vào biến môi trường PATH
Sử dụng với Visual Studio Code
Mở VS Code, tạo file main.py
Dán mã Python vào
Mở Terminal (Ctrl + `)
Cài thư viện nếu chưa có:
- bash
- Sao chép
- Chỉnh sửa
- pip install selenium pandas schedule openpyxl webdriver-manager
Chạy script:
- bash
- Sao chép
- Chỉnh sửa
- python main.py
- Cấu trúc dữ liệu đầu ra
File: batdongsan_output.xlsx
- Tiêu đề
- Mô tả
- Địa chỉ
- Diện tích
- Giá
 Thiết lập lịch chạy tự động
Sử dụng thư viện schedule để chạy hàng ngày lúc 06:00 sáng:
- python
- Sao chép
- Chỉnh sửa
- import schedule
schedule.every().day.at("06:00").do(fetch_data)
 Gồm các file
main.py — mã nguồn chính
requirements.txt — các thư viện cần thiết
