# Lab3: Làm sạch và Tiền xử lý Dữ liệu Nhịp tim

## 1. Giới thiệu
Dự án này thực hiện quy trình **Data Cleaning** (Làm sạch dữ liệu) và **Data Preprocessing** (Tiền xử lý) trên bộ dữ liệu nhịp tim bệnh nhân (`patient_heart_rate.csv`). Mục tiêu là chuyển đổi dữ liệu từ trạng thái thô, lộn xộn sang dạng dữ liệu sạch (Tidy Data) sẵn sàng cho phân tích.

## 2. Các vấn đề chính của dữ liệu thô
* **Cấu trúc không chuẩn:** Cột chứa thông tin hỗn hợp (giới tính + khung giờ đo).
* **Dữ liệu thiếu (Missing Data):** Biến nhịp tim bị thiếu số lượng lớn (> 50%).
* **Lỗi bảng mã (Encoding):** Tên bệnh nhân chứa các ký tự đặc biệt hoặc dấu không đồng nhất.
* **Đơn vị không nhất quán:** Cột cân nặng (`Weight`) chứa cả đơn vị `kgs` và `lbs`.
* **Dữ liệu nhiễu:** Xuất hiện các dòng trống hoặc thông tin không liên quan.

## 3. Quy trình xử lý dữ liệu

### 3.1. Chuẩn hóa cấu trúc (Reshaping)
Sử dụng kỹ thuật **Melt** để chuyển đổi các cột m0006, m0612... thành một cột giá trị nhịp tim duy nhất. Sử dụng **Regex** (Biểu thức chính quy) để tách thông tin:
* `Sex`: m (Nam), f (Nữ).
* `Time`: Khung giờ đo (00-06, 06-12, 12-18).

### 3.2. Tiền xử lý văn bản và đơn vị
* **Xử lý Encoding:** Chuẩn hóa Unicode, loại bỏ dấu tiếng Việt và ký tự lạ trong tên bệnh nhân.
* **Tách cột:** Chia cột `Name` thành `Firstname` và `Lastname`.
* **Chuẩn hóa cân nặng:** Chuyển đổi toàn bộ đơn vị `lbs` về `kg` (1 lb = 0.453592 kg).

### 3.3. Xử lý dữ liệu thiếu (Imputation)
Áp dụng chiến lược điền khuyết phân cấp theo 6 mức ưu tiên:
1. Trung bình giá trị liền trước và liền sau của chính người đó.
2. Trung bình 2 giá trị liền trước của người đó.
3. Trung bình 2 giá trị liền sau của người đó.
4. Trung bình tất cả các giá trị hiện có của người đó.
5. Trung bình theo nhóm giới tính (Nam/Nữ).
6. Trung bình toàn bộ dữ liệu hoặc mức ổn định y học (70 bpm).



### 3.4. Rút gọn và Hoàn thiện
* Loại bỏ các dòng không có đủ thông tin định danh tối thiểu.
* Loại bỏ các bản ghi bị lặp (duplicates).
* Reset lại chỉ số dòng (Reindex) để đảm bảo dữ liệu liên tục.

## 4. Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.x
* **Thư viện chính:**
    * `pandas`: Xử lý và biến đổi cấu trúc bảng.
    * `numpy`: Hỗ trợ các phép toán số học và xử lý NaN.
    * `unicodedata`: Chuẩn hóa bảng mã ký tự.
    * `re`: Xử lý chuỗi bằng Regex.

## 5. Kết quả
* **Tỉ lệ thiếu trước xử lý:** ~54.44%
* **Tỉ lệ thiếu sau xử lý:** 0.00%
* **File kết quả:** `patient_heart_rate_clean.csv`

---
**Người thực hiện:** [Võ Nguyễn Thành Nhân]
**Ngày thực hiện:** 30/01/2026