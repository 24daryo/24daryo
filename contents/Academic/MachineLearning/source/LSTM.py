# Recurrent Neural Network
import tensorflow as tf
from tensorflow.keras import datasets, layers, models, optimizers, callbacks
import numpy as np
import matplotlib.pyplot as plt


# sin関数
def sin(x, T=100):
    return np.sin(2.0 * np.pi * x / T)


# sin波にノイズを付与する
def toy_problem(T=100, ampl=0.05):
    x = np.arange(0, 2 * T + 1)
    noise = ampl * np.random.uniform(low=-1.0, high=1.0, size=len(x))
    return sin(x) + noise


f = toy_problem()


def make_dataset(low_data, n_prev=100):

    data, target = [], []
    maxlen = 25

    for i in range(len(low_data)-maxlen):
        data.append(low_data[i:i + maxlen])
        target.append(low_data[i + maxlen])

    re_data = np.array(data).reshape(len(data), maxlen, 1)
    re_target = np.array(target).reshape(len(data), 1)

    return re_data, re_target


# g -> 学習データ，h -> 学習ラベル
g, h = make_dataset(f)

# モデル構築

# 1つの学習データのStep数(今回は25)
length_of_sequence = g.shape[1]  # 学習データのステップ数
print(length_of_sequence)
input_dimension = 1  # 入力データの次元数(出力も一致)
n_hidden = 300

model = models.Sequential()
model.add(
    layers.LSTM(n_hidden,
                batch_input_shape=(None, length_of_sequence, input_dimension),
                return_sequences=False))
model.add(layers.Dense(input_dimension))
model.add(layers.Activation("linear"))
optimizer = optimizers.Adam(lr=0.001)
model.compile(loss="mean_squared_error", optimizer=optimizer)

early_stopping = callbacks.EarlyStopping(
    monitor='val_loss',
    mode='auto',
    patience=20)
model.fit(g, h,
          batch_size=300,
          epochs=100,
          validation_split=0.1,
          callbacks=[early_stopping]
          )

# 予測
predicted = model.predict(g)

plt.figure()
plt.plot(range(25, len(predicted)+25), predicted,
         color="r", label="predict_data")
plt.plot(range(0, len(f)), f, color="b", label="row_data")
plt.legend()
plt.show()
