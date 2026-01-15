import pandas as pd
import numpy as np

#TAI DU LIEU XET TUYEN DAI HOC
df=pd.read_csv('dulieuxettuyendaihoc.csv',index_col='STT')
df.head(10)

#Thống kê dữ liệu thiếu cho biến T1 và hiệu chỉnh dữ liệu, lưu ý việc thay thế dữ liệu thiếu sử dụng phương pháp Mean.
df['T1']=df['T1'].fillna(df['T1'].mean())
df

#Thống kê dữ liệu thiếu cho cột dân tộc và hiệu chỉnh dữ liệu thiếu như sau: Mặc định thiếu thì điền giá trị 0.
df['DT']=df['DT'].fillna(0)
df

#Hãy thực hiện xử lý lần lượt tất cả dữ liệu thiếu cho các biến về điểm số còn lại.
subjects = ['T', 'L', 'H', 'S', 'V', 'X', 'D', 'N']
score_numbers = range(1, 7) # Từ 1 đến 6
col_score = [f"{s}{n}" for s in subjects for n in score_numbers]

for i in col_score:
    df[i] = df[i].fillna(df[i].mean())
df = df.round(1)
df

#7.Tạo các biến TBM1, TBM2, TBM3 tương ứng với trung bình môn của các năm lớp 10, 11 và 12.
#• Công thức tính: TBM = (T*2 + L + H + S + V*2 + X + D + N) / 10

# Đọc dữ liệu
df = pd.read_csv('dulieuxettuyendaihoc.csv')

# Tính toán TBM1 (Lớp 10 - HK1)
df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['S1'] + df['V1']*2 + df['X1'] + df['D1'] + df['N1']) / 10

# Tính toán TBM2 (Lớp 10 - HK2)
df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['S2'] + df['V2']*2 + df['X2'] + df['D2'] + df['N2']) / 10

# Tính toán TBM3 (Lớp 12 - HK2)
df['TBM3'] = (df['T6']*2 + df['L6'] + df['H6'] + df['S6'] + df['V6']*2 + df['X6'] + df['D6'] + df['N6']) / 10

# Lưu kết quả vào file mới
df.to_csv('dulieuxettuyendaihoc_updated.csv', index=False)

# Hiển thị 5 dòng đầu tiên của các cột mới tính
print(df[['TBM1', 'TBM2', 'TBM3']].head())

#Tạo các biến xếp loại XL1, XL2 và XL3 dựa trên TBM1,TBM2 và TBM3 cho từng năm lớp
#10, 11, 12 như sau:
#• Nhỏ hơn 5.0 xếp loại: yếu (kí hiệu là Y)
#• Từ 5.0 đến dưới 6.5: trung bình (kí hiệu là TB)
#• Từ 6.5 đến dưới 8.0: khá (kí hiệu là K)
#• Từ 8.0 đến dưới 9.0: giỏi (kí hiệu là G)
#• Từ 9.0 trở lên: xuất sắc (kí hiệu là XS)

# 1. Đọc dữ liệu từ file CSV
df = pd.read_csv('dulieuxettuyendaihoc.csv')

# 2. Hàm tính điểm trung bình môn (TBM) theo công thức
# Tính toán TBM1 (Lớp 10 - HK1)
df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['S1'] + df['V1']*2 + df['X1'] + df['D1'] + df['N1']) / 10

# Tính toán TBM2 (Lớp 10 - HK2)
df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['S2'] + df['V2']*2 + df['X2'] + df['D2'] + df['N2']) / 10

# Tính toán TBM3 (Lớp 12 - HK2)
df['TBM3'] = (df['T6']*2 + df['L6'] + df['H6'] + df['S6'] + df['V6']*2 + df['X6'] + df['D6'] + df['N6']) / 10

# 3. Hàm xếp loại (XL) dựa trên điểm TBM
def xep_loai(tbm):
    if tbm < 5.0:
        return 'Y'
    elif tbm < 6.5:
        return 'TB'
    elif tbm < 8.0:
        return 'K'
    elif tbm < 9.0:
        return 'G'
    else:
        return 'XS'

# Áp dụng hàm xếp loại cho từng năm
df['XL1'] = df['TBM1'].apply(xep_loai)
df['XL2'] = df['TBM2'].apply(xep_loai)
df['XL3'] = df['TBM3'].apply(xep_loai)

# 4. Hiển thị kết quả kiểm tra (10 dòng đầu tiên)
print("Kết quả tính toán TBM và Xếp loại:")
columns_to_show = ['TBM1', 'XL1', 'TBM2', 'XL2', 'TBM3', 'XL3']
print(df[columns_to_show].head(10))

# 5. Lưu kết quả ra file CSV mới
df.to_csv('ketqua_xet_tuyen.csv', index=False)
print("\nĐã lưu kết quả vào file 'ketqua_xet_tuyen.csv'")

#Tạo các biến US_TBM1, US_TBM2 và US_TBM3 để chuyển điểm trung bình các năm lớp
#10, 11 và 12 từ thang điểm 10 của Việt Nam sang thang điểm 4 của Mỹ. Sử dụng phương
#pháp Min-Max Normalization

# 1. Đọc dữ liệu từ file đã có sẵn TBM
df = pd.read_csv('ketqua_xet_tuyen.csv')

# 2. Tạo các biến US_TBM1, US_TBM2, US_TBM3 bằng Min-Max Normalization
# Chuyển từ [0, 10] sang [0, 4]
df['US_TBM1'] = (df['TBM1'] / 10) * 4
df['US_TBM2'] = (df['TBM2'] / 10) * 4
df['US_TBM3'] = (df['TBM3'] / 10) * 4

# 3. Hiển thị kết quả kiểm tra (5 dòng đầu)
print("Kết quả chuyển đổi sang thang điểm Mỹ (4.0):")
print(df[['TBM1', 'US_TBM1', 'TBM2', 'US_TBM2', 'TBM3', 'US_TBM3']].head())

# 4. Lưu kết quả ra file CSV mới
df.to_csv('dulieu_chuanhoa.csv', index=False)

#Tạo biến kết quả xét tuyển (kí hiệu là KQXT) nhằm xác định sinh viên đậu (giá trị “1”) và
#rớt ( giá trị “0”) vào các khối dựa trên điểm DH1, DH2 và DH3 như sau
#• Với khối A, A1 nếu [(DH1*2 + DH2 + DH3)/4] lớn hơn hoặc bằng 5.0 thì đậu,
#ngược lại là rớt
#• Với khối B nếu [(DH1 + DH2*2 + DH3)/4] lớn hơn hoặc bằng 5.0 thì đậu, ngược
#lại là rớt
#• Với khối khác nếu [(DH1+ DH2 + DH3)/3] lớn hơn hoặc bằng 5.0 thì đậu, ngược lại là rớt

# 1. Đọc dữ liệu từ file đã có
df = pd.read_csv('dulieu_chuanhoa.csv')

# 2. Định nghĩa hàm tính toán kết quả xét tuyển
def tinh_kqxt(row):
    kt = row['KT']      # Khối thi
    dh1 = row['DH1']    # Điểm môn 1
    dh2 = row['DH2']    # Điểm môn 2
    dh3 = row['DH3']    # Điểm môn 3

    # Tính điểm xét tuyển dựa trên khối
    if kt in ['A', 'A1']:
        diem_xt = (dh1 * 2 + dh2 + dh3) / 4
    elif kt == 'B':
        diem_xt = (dh1 + dh2 * 2 + dh3) / 4
    else: # Các khối khác (C, D1,...)
        diem_xt = (dh1 + dh2 + dh3) / 3

    # Trả về 1 nếu đậu (>= 5.0), ngược lại trả về 0
    return 1 if diem_xt >= 5.0 else 0

# 3. Áp dụng hàm để tạo biến KQXT
df['KQXT'] = df.apply(tinh_kqxt, axis=1)

# 4. Hiển thị kết quả kiểm tra (10 dòng đầu)
print("Kết quả xét tuyển theo khối:")
print(df[['KT', 'DH1', 'DH2', 'DH3', 'KQXT']].head(10))

# 5. Lưu kết quả ra file CSV cuối cùng
df.to_csv('ketqua_xettuyen_final.csv', index=False)

#Lưu trữ dữ liệu xuống ổ đĩa thành file processed_dulieuxettuyendaihoc.csv

# 1. Đọc dữ liệu từ kết quả xử lý gần nhất
# Giả sử bạn đang tiếp tục từ file 'ketqua_xettuyen_final.csv'
df = pd.read_csv('ketqua_xettuyen_final.csv')

# 2. Lưu trữ dữ liệu xuống ổ đĩa với tên file mới
df.to_csv('processed_dulieuxettuyendaihoc.csv', index=False)

print("Đã lưu trữ dữ liệu thành công vào file: processed_dulieuxettuyendaihoc.csv")
