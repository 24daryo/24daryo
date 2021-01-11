import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# MNIST(0~9の文字認識用データセット)をロード
(train_images, train_labels), (test_images,
                               test_labels) = datasets.mnist.load_data()

# サイズを28*28の白黒画像に変換
train_images = train_images.reshape((60000, 28, 28, 1))  # 60000枚の画像
test_images = test_images.reshape((10000, 28, 28, 1))  # 10000枚の画像


# ピクセルの値を 0~1 の間に正規化
train_images, test_images = train_images / 255.0, test_images / 255.0

# Convolution部分のネットワークを生成(前半部分)
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# 通常のネットワークを生成(後半部分)
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# モデルをコンパイル
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# データを入力して学習させる
model.fit(train_images, train_labels, epochs=1)

# テストデータを入力し評価する
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(f"誤差：{test_loss}")
print(f"精度：{test_acc}")
