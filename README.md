# Bài toán vận tải
Chương trình có thể giúp người dùng đưa ra cách thức vận chuyển hàng hoá sao cho tiết kiệm chi phí vận chuyển nhất
## Thông tin:
- **Họ và tên:** Lê Bá Nguyên
- **Tên**: Bài toán vận tải
## Tính năng:
- Đưa ra các hướng dẫn nhằm vận chuyển hàng từ các điểm cung đến các điểm cầu sao cho tổng chi phí vận chuyển là ít nhất
## Hướng dẫn sử dụng:
- Đầu tiên: ta nhập từ bàn phím số lượng khu vực các điểm kinh tế (hay còn gọi là số lượng kho hàng), kí hiệu là m
- Ta nhập tiếp khối lượng hàng hoá của từng kho hàng

![image](https://github.com/user-attachments/assets/9f5d8683-bdf9-4874-aaf0-63d9d3ee938e)

- Sau đó: ta nhập từ bàn phím số lượng điểm tiêu thụ hàng, kí hiệu là n 
- Ta nhập tiếp khối lượng hàng hoá theo nhu cầu của từng điểm

![image](https://github.com/user-attachments/assets/68214452-5539-413d-8bde-01251bd17ea5)

- Với mỗi điểm kinh tế kí hiệu là A_i (với i chạy từ 1 đến m) ta có n điểm tiêu thụ hàng, kí hiệu là B_j (với j chạy từ 1 đến n).
- Ta nhập số tiền vận chuyển cho từng chuyến hàng từ A_i đến B_j
- Ví dụ: với số lượng kho hàng m=2 và số lượng điểm tiêu thụ hàng n=2 ta có:
+ Nhập chi phí vận chuyển từ A1 đến B1: 200000
+ Nhập chi phí vận chuyển từ A1 đến B2: 150000
+ Nhập chi phí vận chuyển từ A2 đến B1: 230000
+ Nhập chi phí vận chuyển từ A2 đến B2: 170000
(Lưu ý: các số m, n, 200000, 1500000, 230000, 170000 là các số do người viết tự đặt, khi chạy lệnh bạn hãy nhập dữ liệu sao cho phù hợp với bài toán của bạn)
- Chương trình trả về tổng số tiền vận chuyển và phương hướng vận chuyển sao cho hiệu quả nhất
- Lưu ý: Một biến giả A_m+1 (hoặc B_n+1) khi cung (hoặc cầu) bé hơn cái còn lại
## Lưu ý:
- Ưu tiên chương trình hoạt động trên điều hành Windows
- Vui lòng tải thư viện numpy của python trước khi chạy chương trình
