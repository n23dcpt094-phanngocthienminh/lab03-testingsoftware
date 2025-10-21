# Hướng Dẫn Setup & Chạy Test (Lab 03 - Testing Login Form)

## 1. Mục tiêu
Kiểm thử form đăng nhập (Login Form) bằng Selenium + Python + pytest  
Bao gồm 6 test case kiểm tra các chức năng cơ bản: đăng nhập, lỗi đăng nhập, bỏ trống, forgot password, sign up, social login.

---

## 2. Cài đặt môi trường

### 🔹 Bước 1: Cài Python
Tải & cài Python 3.x tại: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
Khi cài, nhớ tick **“Add Python to PATH”**

---

### 🔹 Bước 2: Cài thư viện Selenium & Pytest
Mở **Terminal** hoặc **PowerShell**, gõ:

```bash
pip install selenium pytest
```

Nếu dùng **Python 3** thì gõ:
```bash
pip3 install selenium pytest
```

---

### 🔹 Bước 3: Cài ChromeDriver
1. Kiểm tra phiên bản Chrome của bạn:  
   - Mở Chrome → Gõ `chrome://settings/help`  
2. Truy cập: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)  
3. Tải bản ChromeDriver **cùng phiên bản**  
4. Giải nén và đặt file `chromedriver.exe` trong thư mục project hoặc thêm vào PATH

---

### 🔹 Bước 4: Cấu trúc thư mục

```
📂 login-test
 ├── test_login.py       # File code kiểm thử Selenium
 ├── test_cases.txt      # Liệt kê test case
 ├── GUIDE.md            # File hướng dẫn setup & chạy test
 ├── README.md           # Use case + mô tả bài lab
 └── screenshots/        # Ảnh chụp kết quả chạy test
```

---

## 3. Chạy test

### ▶ Cách chạy
Mở terminal trong VS Code hoặc CMD tại thư mục chứa file test:
```bash
pytest test_login.py -v
```

### ▶ Kết quả hiển thị (ví dụ)
```
=========================== test session starts ===========================
collected 6 items

test_login.py::test_login_success PASSED                          [ 16%]
test_login.py::test_login_wrong_password PASSED                   [ 33%]
test_login.py::test_blank_username PASSED                         [ 50%]
test_login.py::test_blank_password PASSED                         [ 66%]
test_login.py::test_forgot_password_link PASSED                   [ 83%]
test_login.py::test_social_login_buttons PASSED                   [100%]

============================ 6 passed in 10.2s ============================
```

### ▶ Khi hoàn tất:
- Toàn bộ 6 test case **PASS** → đạt 6 điểm phần chạy.  
- Chụp ảnh màn hình kết quả này để đưa vào báo cáo.  

---

## 4. Lưu ý
- Nếu test không chạy, kiểm tra lại `chromedriver` hoặc URL trang login.  
- Có thể thay đường dẫn:
  ```python
  driver.get("http://localhost:8000/login")
  ```
  thành URL thật mà bạn dùng.

---

✅ **Hoàn thành:**  
Sau khi chạy test thành công, post toàn bộ lên GitHub gồm:
- README.md  
- GUIDE.md  
- test_login.py  
- test_cases.txt  
- Ảnh chụp kết quả chạy test  
