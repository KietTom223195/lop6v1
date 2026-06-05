# 🌸 Iris Species Classifier - Interactive ANN Visualizer

Một ứng dụng Web tĩnh (Single Page Application) trực quan hóa cấu trúc và hoạt động của **Mạng Nơ-ron Nhân tạo (ANN)** trong bài toán phân loại các loài hoa Iris (Hoa diên vĩ) dựa trên các đặc trưng kích thước lá đài và cánh hoa.

Dự án được thiết kế tối giản, chạy hoàn toàn ở phía client (trình duyệt) với hiệu ứng thị giác **Glassmorphism** hiện đại và đồ họa nơ-ron truyền tín hiệu động bằng SVG.

> [!TIP]
> Bạn có thể chạy trực tiếp dự án này trên web bằng cách kích hoạt tính năng **GitHub Pages** chỉ với vài cú click chuột!

---

## ✨ Các tính năng nổi bật

* 🌐 **Chạy Offline 100%:** Không cần cài đặt Python, TensorFlow hay bất kỳ thư viện nặng hàng gigabyte nào trên máy. Chỉ cần một tệp `index.html` duy nhất.
* 🧠 **Mô phỏng mạng ANN trực quan:** Trực quan hóa kiến trúc mạng nơ-ron chuỗi (Sequential) gồm **4 đầu vào -> 8 nơ-ron ẩn -> 6 nơ-ron ẩn -> 3 đầu ra**.
* ⚡ **Tương tác thời gian thực (Real-time):** Khi điều chỉnh kích thước Lá đài (Sepal) và Cánh hoa (Petal) bằng các thanh trượt, luồng truyền tín hiệu và các nơ-ron tương ứng trên đồ thị SVG sẽ tự động phát sáng dựa trên mức độ kích hoạt (Activation).
* 📊 **Xác suất Softmax chính xác:** Hiển thị phân bố xác suất dự đoán của 3 loài hoa (Setosa, Versicolor, Virginica) dưới dạng thanh tiến trình (progress bars) động.
* 🎨 **Giao diện Premium:** Thiết kế tối màu (Dark Mode) sang trọng, kết hợp font chữ *Plus Jakarta Sans* và các dải màu chuyển sắc (gradients) hài hòa cho từng loài hoa.

---

## 🚀 Hướng dẫn chạy nhanh trên máy cá nhân

### Cách 1: Kích đúp mở trực tiếp
1. Tải tệp [index.html](index.html) về máy tính của bạn.
2. Kích đúp chuột trực tiếp vào tệp `index.html` để mở bằng bất kỳ trình duyệt web nào (Chrome, Edge, Firefox, Safari...).

### Cách 2: Sử dụng Live Server trong VS Code
1. Mở thư mục chứa dự án bằng phần mềm **VS Code**.
2. Đảm bảo đã cài đặt Extension **Live Server** của VS Code.
3. Nhấp chuột phải vào tệp `index.html` và chọn **Open with Live Server**.

---

## 🌐 Hướng dẫn đưa lên GitHub Pages (Để chạy trực tiếp trên Internet)

Nếu bạn muốn tạo một đường link web cá nhân (ví dụ: `https://username.github.io/ten-kho-chua/`) để khoe bài làm hoặc chia sẻ cho thầy cô/bạn bè:

1. **Tạo Kho chứa (Repository) mới trên GitHub:**
   - Đăng nhập vào GitHub, chọn **New Repository**.
   - Đặt tên cho kho chứa (ví dụ: `iris-ann-visualizer`).
   - Chọn chế độ **Public** và bấm **Create repository**.

2. **Tải tệp `index.html` lên kho chứa:**
   - Trong trang kho chứa vừa tạo, chọn **uploading an existing file**.
   - Kéo tệp `index.html` từ máy tính của bạn vào và chọn **Commit changes**.

3. **Kích hoạt GitHub Pages:**
   - Vào mục **Settings** (Cài đặt) của kho chứa đó trên GitHub.
   - Chọn mục **Pages** ở thanh menu bên trái.
   - Tại phần **Branch**, đổi từ `None` thành `main` (hoặc `master`), giữ nguyên thư mục `/ (root)` và bấm **Save**.
   - Đợi khoảng 1 - 2 phút, GitHub sẽ cung cấp một đường link hiển thị trực tiếp ứng dụng web của bạn trên internet!

---

## 📐 Kiến trúc mạng Nơ-ron (ANN Model)

Mô hình được thiết kế dựa trên yêu cầu của bài tập lớn môn Học máy / Trí tuệ nhân tạo:
- **Tầng đầu vào (Input Layer):** 4 đặc trưng kích thước của hoa diên vĩ (Sepal Length, Sepal Width, Petal Length, Petal Width).
- **Tầng ẩn 1 (Hidden Layer 1):** 8 nơ-ron sử dụng hàm kích hoạt **ReLU**.
- **Tầng ẩn 2 (Hidden Layer 2):** 6 nơ-ron sử dụng hàm kích hoạt **ReLU**.
- **Tầng đầu ra (Output Layer):** 3 nơ-ron (Setosa, Versicolor, Virginica) sử dụng hàm kích hoạt **Softmax** để đưa ra phân phối xác suất.

---

## 👤 Thông tin tác giả & Bản quyền

Dự án được xây dựng phục vụ cho mục đích học tập môn Học máy và Trí tuệ nhân tạo. 
* Lập trình bởi: **Antigravity AI Assistant & Bạn**
* Giấy phép sử dụng: **MIT License**
