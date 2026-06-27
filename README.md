# K-Means Clustering Visualization

Đây là một ứng dụng trực quan hóa thuật toán phân cụm K-Means được viết bằng Python. Ứng dụng cung cấp giao diện đồ họa tương tác giúp người dùng dễ dàng quan sát cách thuật toán gom cụm dữ liệu từng bước hoặc giải quyết tức thì bằng thư viện học máy.

## Tính năng nổi bật

*   **Tương tác trực tiếp:** Nhấp chuột vào khu vực bảng điều khiển (panel) để tạo các điểm dữ liệu tùy ý.
*   **Điều chỉnh số cụm (K):** Sử dụng nút `+` và `-` để thay đổi số lượng cụm K (hỗ trợ phân biệt tối đa 8 cụm bằng 8 màu sắc khác nhau).
*   **Khởi tạo ngẫu nhiên:** Nút `Random` cho phép tạo ngẫu nhiên vị trí của các tâm cụm (centroids) trong phạm vi màn hình vẽ.
*   **Chạy từng bước (Manual Mode):** Nhấn nút `Run` để tính toán khoảng cách, gán điểm vào cụm gần nhất và cập nhật lại vị trí tâm cụm theo từng bước thủ công.
*   **Chạy tự động (Auto Mode):** Nút `Algorithm` tích hợp sẵn mô hình `KMeans` từ thư viện `scikit-learn` (với `n_init=10`) để tính toán và phân cụm dữ liệu tức thì.
*   **Tính toán sai số:** Hiển thị trực tiếp chỉ số sai số (Error) dựa trên tổng khoảng cách từ các điểm dữ liệu đến tâm cụm tương ứng của chúng.
*   **Làm mới (Reset):** Nút `Reset` giúp xóa toàn bộ điểm dữ liệu, tâm cụm, đặt lại thông số K và Error về 0.
*   **Hiển thị tọa độ:** Tự động theo dõi và hiển thị tọa độ con trỏ chuột khi di chuyển trong khu vực vẽ.

## Yêu cầu môi trường

Để chạy được đoạn mã này, hệ thống của bạn cần cài đặt Python và các thư viện đi kèm sau:
*   `pygame`
*   `scikit-learn`

Bạn có thể cài đặt nhanh các thư viện yêu cầu thông qua `pip`:
pip install -r requirements.txt

## Hướng dẫn sử dụng

1. Mở Terminal / Command Prompt và chạy file mã nguồn:
   python <tên_file_của_bạn>.py
2. Giao diện chương trình sẽ mở ra. Hãy click chuột vào khung nền để thêm các điểm dữ liệu.
3. Nhấn nút `+` trên giao diện để thiết lập giá trị K (số lượng cụm).
4. Nhấn `Random` để khởi tạo các điểm tâm cụm ngẫu nhiên.
5. Nhấn `Run` liên tục để quan sát thuật toán tự động điều chỉnh vị trí các tâm cụm cho đến khi tối ưu.
6. Nhấn `Algorithm` nếu muốn xem ngay kết quả tối ưu mà không cần chạy từng bước.
7. Nhấn `Reset` để bắt đầu lại một mô phỏng mới.