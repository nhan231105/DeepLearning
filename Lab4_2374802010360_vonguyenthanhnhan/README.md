1. Mục tiêu: Làm sạch dữ liệu và tạo ra các biến mới có ý nghĩa thống kê hơn để phục vụ cho việc phân tích hoặc huấn luyện mô hình máy học.

2. Các bước thực hiện chính:

Tạo đặc trưng FamilySize (Kích thước gia đình):

Tính tổng số lượng thành viên đi cùng một nhóm gia đình.

Công thức: FamilySize = 1 (bản thân) + SibSp (anh chị em/vợ chồng) + Parch (bố mẹ/con cái).

Tạo đặc trưng Alone (Đi một mình):

Xác định xem hành khách có đi một mình hay không dựa trên FamilySize.

Quy tắc: Nếu FamilySize = 1 thì Alone = 1 (Đúng), ngược lại Alone = 0 (Sai).

Xử lý thông tin Cabin (typeCabin):

Trích xuất chữ cái đầu tiên trong cột Cabin để xác định loại boong tàu/khu vực (ví dụ: C85 -> C).

Xử lý dữ liệu thiếu: Các ô trống (NaN) được điền giá trị là "Unknown" để không làm mất thông tin.

Lọc dữ liệu trùng lặp (De-duplication):

Xử lý trường hợp một hành khách xuất hiện ở cả hai tập dữ liệu (huấn luyện và kiểm thử).

Quy tắc: Ưu tiên giữ lại dữ liệu trong tập huấn luyện (train), loại bỏ dữ liệu trùng khớp trong tập kiểm thử (test) dựa trên PassengerId.

3. Kết quả đạt được: Bộ dữ liệu sau khi xử lý sẽ có thêm các cột thông tin giàu ý nghĩa (FamilySize, Alone, typeCabin) và đảm bảo tính nhất quán, không trùng lặp giữa các tập dữ liệu.