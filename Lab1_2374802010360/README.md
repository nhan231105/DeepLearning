


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
Tổng quan quá trình thực hiện chuỗi bài tập xử lý dữ liệu xét tuyển đại học:

1. Công nghệ sử dụng
Ngôn ngữ lập trình: Python.

Thư viện chính: Pandas (Thư viện hàng đầu để thao tác và phân tích dữ liệu dạng bảng/Dataframe).

Công cụ: Môi trường lập trình (như Jupyter Notebook, Google Colab hoặc trình thông dịch Python).

Định dạng dữ liệu: CSV (Comma Separated Values).

2. Cách hoạt động (Quy trình xử lý)
Quá trình xử lý dữ liệu được thực hiện theo luồng khoa học (Data Pipeline):

Bước 1: Nhập liệu & Khám phá: Sử dụng pd.read_csv để đưa dữ liệu vào hệ thống. Xem xét cấu trúc cột để hiểu ý nghĩa từng biến số (Điểm thi, thông tin cá nhân, khối thi).

Bước 2: Phân loại & Định nghĩa thang đo: Xác định các biến định tính (như Giới tính, Khối thi) và định lượng (như Điểm số). Hiệu chỉnh kiểu dữ liệu (category cho định danh, float cho tỉ lệ) để máy tính hiểu đúng tính chất vật lý của dữ liệu.

Bước 3: Xử lý dữ liệu thiếu (Cleaning): Kiểm tra và loại bỏ hoặc thay thế các giá trị trống (NaN) để đảm bảo tính nhất quán.

Bước 4: Chuyển đổi dữ liệu (Transformation): Áp dụng phương pháp Min-Max Normalization để đưa điểm số từ thang 10 (Việt Nam) về thang 4 (Mỹ), giúp dữ liệu dễ so sánh quốc tế.

Bước 5: Kỹ thuật đặc trưng (Feature Engineering):

Sử dụng công thức nghiệp vụ (Weighted Mean) để tính điểm trung bình (TBM).

Sử dụng logic điều kiện (if-else) để tạo các biến mới như Xếp loại (XL) và Kết quả xét tuyển (KQXT) dựa trên các biến độc lập có sẵn.

Bước 6: Lưu trữ: Xuất kết quả cuối cùng ra file .csv mới để phục vụ lưu trữ hoặc báo cáo.

3. Kết quả đạt được
Từ một file dữ liệu thô ban đầu chỉ có các đầu điểm thành phần, chúng ta đã tạo ra một bộ dữ liệu hoàn chỉnh (processed_dulieuxettuyendaihoc.csv) với các thông tin giá trị cao:

Hệ thống điểm trung bình (TBM1, 2, 3): Phản ánh chính xác học lực theo trọng số của từng năm học.

Hệ thống xếp loại (XL1, 2, 3): Chuyển đổi từ dữ liệu số sang dữ liệu định tính (Y, TB, K, G, XS) để dễ dàng đánh giá học lực học sinh.

Hệ thống điểm chuẩn quốc tế (US_TBM): Giúp học sinh/nhà quản lý so sánh năng lực trên thang điểm toàn cầu.

Kết quả xét tuyển (KQXT): Xác định chính xác tình trạng Đậu/Rớt (1/0) dựa trên quy tắc tuyển sinh phức tạp của từng khối thi (A, B, C...).

Cấu trúc dữ liệu chuẩn: Các biến số được gắn đúng thang đo (Nominal, Ordinal, Ratio), sẵn sàng để đưa vào các mô hình học máy (Machine Learning) hoặc vẽ biểu đồ thống kê trực quan.
