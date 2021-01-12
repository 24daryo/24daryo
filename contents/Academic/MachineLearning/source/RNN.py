# Recurrent Neural Network
# オプティマイザーは以下参照
# https://keras.io/ja/optimizers/
# 参考
# https://qiita.com/everylittle/items/c088564d53cdfcde92cc#fn1
import tensorflow as tf
import numpy as np
from tensorflow.keras import Sequential, layers, optimizers

# 初期シードを生成
tf.random.set_seed(111)
np.random.seed(111)

# RNNを生成
model = Sequential()
input_dim = 1
output_dim = 1
model.add(layers.SimpleRNN(output_dim, activation=None,
                           input_shape=(None, input_dim), return_sequences=True))
# コンパイル
model.compile(optimizer=optimizers.Adam(lr=0.001), loss="mean_squared_error")

# 学習データを用意
n = 51200                           # 学習データ数
step = 10                           # 時系列データの数
x = np.random.random((n, step, 1))  # x = [X1, X2, ..., X10]。51200個の学習データあり
y = x.cumsum(axis=1)                # y = [Y1, Y2, ..., Y10]。例：Y3 = X1+X2+X3

# 学習
model.fit(x, y, batch_size=512, epochs=100)

# 学習結果をもとに予想(10個先の未来も予想)
test_x = np.ones((1, step+10, 1))
test_y = model.predict(test_x)
print("⭐️学習結果⭐️")
print(test_x.flatten())
print(test_y.flatten())
