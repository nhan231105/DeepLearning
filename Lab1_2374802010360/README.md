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
