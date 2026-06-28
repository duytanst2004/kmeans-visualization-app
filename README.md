# KMeans Visualization

Ứng dụng trực quan hóa thuật toán **K-Means Clustering** theo thời gian thực, xây dựng bằng `pygame`. Người dùng có thể tự đặt điểm dữ liệu, chọn số cụm K, chạy từng bước lặp thủ công hoặc để scikit-learn giải quyết toàn bộ.

---

## Tính năng

- **Thêm điểm dữ liệu** bằng cách click trực tiếp lên canvas
- **Điều chỉnh K** (số cụm) với nút `+` / `-`
- **Khởi tạo ngẫu nhiên** các tâm cụm (centroids)
- **Chạy từng bước** (E-step + M-step) để quan sát quá trình hội tụ
- **Chạy scikit-learn KMeans** để so sánh kết quả
- **Hiển thị Error** (tổng khoảng cách điểm → tâm cụm)
- **Reset** toàn bộ về trạng thái ban đầu

---

## Cấu trúc dự án

```
kmeans_algorithm/
├── main.py             # Vòng lặp game chính, render và xử lý event
├── config.py           # Hằng số: màu sắc, kích thước cửa sổ, layout
├── button.py           # Class TextButton
├── utils.py            # Hàm distance(), build_buttons()
├── kmeans_handler.py   # Logic clustering (random init, E/M-step, sklearn)
└── README.md
```

---

## Yêu cầu

- Python 3.8+
- pygame
- scikit-learn

---

## Cài đặt

```bash
# 1. Clone repo
git clone https://github.com/duytanst2004/kmeans-algorithm.git
cd kmeans-algorithm

# 2. Tạo môi trường ảo (khuyến nghị)
python -m venv venv
venv\Scripts\activate

# 3. Cài dependencies
pip install -r requirements.txt
```

---

## Chạy ứng dụng

```bash
python main.py
```

---

## Hướng dẫn sử dụng

| Thao tác          | Mô tả                                   |
| ----------------- | --------------------------------------- |
| Click vào canvas  | Thêm một điểm dữ liệu                   |
| Nút `+` / `-`     | Tăng / giảm số cụm K                    |
| Nút **Random**    | Khởi tạo K tâm cụm ở vị trí ngẫu nhiên  |
| Nút **Run**       | Thực hiện một bước lặp E-step + M-step  |
| Nút **Algorithm** | Chạy scikit-learn KMeans đến khi hội tụ |
| Nút **Reset**     | Xóa tất cả, bắt đầu lại                 |

### Quy trình khuyến nghị

1. Click để thêm các điểm dữ liệu lên canvas
2. Dùng `+` để chọn K (số cụm mong muốn)
3. Nhấn **Random** để đặt các tâm cụm ban đầu
4. Nhấn **Run** nhiều lần để thấy từng bước hội tụ
5. So sánh với **Algorithm** (kết quả của scikit-learn)

---

## Mô tả thuật toán K-Means

K-Means chia tập dữ liệu thành K cụm bằng cách lặp lại 2 bước:

```
Repeat until convergence:
  E-step: Gán mỗi điểm vào cụm có tâm gần nhất
  M-step: Cập nhật tâm cụm = trung bình các điểm thuộc cụm đó
```

**Error** hiển thị trên giao diện là tổng khoảng cách Euclidean từ mỗi điểm đến tâm cụm của nó — giá trị này giảm dần qua mỗi lần nhấn **Run**.

---
