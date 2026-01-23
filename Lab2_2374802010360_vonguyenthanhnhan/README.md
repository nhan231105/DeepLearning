


📊 Lab 2: Phân tích và Trực quan hóa Dữ liệu Xét tuyển Đại học

Tác giả: Võ Nguyễn Thành Nhân

MSSV: 2374802010360

Môn học: Deep Learning 

📝 Giới thiệu
Dự án này là bài thực hành Lab 2, tập trung vào việc sử dụng Python để phân tích thống kê mô tả và trực quan hóa dữ liệu từ tập tin processed_dulieuxettuyendaihoc.csv.

Mục tiêu chính là khảo sát phân phối của điểm Toán học kỳ 1 lớp 10 (biến T1), phân loại học lực, và đánh giá mối tương quan giữa kết quả học tập phổ thông với kết quả thi đại học.

📂 Cấu trúc Notebook
Bài làm được chia thành 2 phần chính:

Phần 1: Thống kê dữ liệu (Data Statistics)
Mô tả biến T1 (Điểm Toán HK1 lớp 10):

Tính toán các đại lượng thống kê: Mean, Median, Mode, Min, Max, Std, Skewness, Kurtosis.

Kết quả cho thấy phân phối điểm hơi lệch trái và có đỉnh bẹt (Platykurtic).

Phân loại biến T1:

Tạo biến phân loại phanlopt1 với các nhóm: Kém (k), Trung bình (tb), Giỏi (g).

Lập bảng tần số cho biến phân loại.

Thống kê theo nhóm:

Tính các đại lượng thống kê mô tả chi tiết cho từng nhóm học lực.

Phần 2: Trực quan hóa dữ liệu (Data Visualization)
Sử dụng thư viện Matplotlib và Seaborn để vẽ các biểu đồ:

Biểu đồ đường (Line Plot):

Biểu đồ Simple Line cho biến T1.

Biểu đồ Multiple Line so sánh các nhóm phân loại (k, tb, g).

Biểu đồ Drop-line (Lollipop) để hiển thị giá trị cụ thể.

Biểu đồ phân phối:

Box-plot: So sánh độ phân tán và nhận diện ngoại lai giữa các nhóm.

Histogram: Xem hình dáng phân phối xác suất.

QQ-Plot: Kiểm định phân phối chuẩn của dữ liệu.

Biểu đồ tương quan (Correlation):

Scatter Plot: Khảo sát mối quan hệ giữa điểm học bạ (T1) và điểm thi đại học môn Toán (DH1).

Scatter by Group: Phân tích tương quan T1 - DH1 theo từng khu vực (KV).

Pairplot/Heatmap: Đánh giá sự độc lập giữa 3 môn thi đại học Toán (DH1), Văn (DH2), Anh (DH3).

🛠️ Công nghệ sử dụng
Ngôn ngữ: Python 

Môi trường: Google Colab / Jupyter Notebook

Thư viện:

pandas: Xử lý và phân tích dữ liệu dạng bảng.

numpy: Tính toán khoa học.

matplotlib: Vẽ biểu đồ cơ bản.

seaborn: Vẽ biểu đồ thống kê nâng cao và đẹp mắt.

scipy: Tính toán các chỉ số thống kê (skew, kurtosis).
---------------------------------------------------------
