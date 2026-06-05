import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# --- BƯỚC 1: TẢI VÀ CHUẨN BỊ DỮ LIỆU ---
iris = load_iris()
X = iris.data  
y = iris.target.reshape(-1, 1)  

# Mã hóa nhãn sang dạng One-Hot Vector
encoder = OneHotEncoder(sparse_output=False)
y_onehot = encoder.fit_transform(y)

# Chia dữ liệu thành tập Train (80%) và Test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

# --- BƯỚC 2: XÂY DỰNG CẤU TRÚC MẠNG ANN ---
model = Sequential()
model.add(Dense(8, input_shape=(4,), activation='relu')) # Tầng ẩn 1
model.add(Dense(6, activation='relu'))                   # Tầng ẩn 2
model.add(Dense(3, activation='softmax'))                # Tầng đầu ra

model.summary()

# --- BƯỚC 3: CẤU HÌNH QUY TRÌNH HUẤN LUYỆN ---
model.compile(optimizer=Adam(learning_rate=0.01),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# --- BƯỚC 4: TIẾN HÀNH HUẤN LUYỆN ---
print("\n--- Bắt đầu huấn luyện mạng ANN ---")
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1)

# --- BƯỚC 5: ĐÁNH GIÁ MÔ HÌNH ---
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n ĐỘ CHÍNH XÁC TRÊN TẬP KIỂM TRA: {accuracy * 100:.2f}%")

# --- BƯỚC 6: DỰ ĐOÁN THỰC TẾ ---
# Dữ liệu đo đạc của một bông hoa mới:
hoa_moi = np.array([[5.1, 3.5, 1.4, 0.2]])
du_doan = model.predict(hoa_moi)
loai_hoa_du_doan = np.argmax(du_doan)

print(f"Xác suất dự đoán cho 3 loài hoa lần lượt là: {du_doan}")
print(f"-> Kết quả dự đoán loài hoa mang nhãn số: {loai_hoa_du_doan} ({iris.target_names[loai_hoa_du_doan].upper()})")
