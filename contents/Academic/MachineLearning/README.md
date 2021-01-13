# 機械学習の実装

## ３層構造ニューラルネットワーク

入力層 X、中間層 Y、出力層 Z で構成されたネットワーク

学習用のため numpy のみで実装

ほとんど以下の記事を参考にしました

https://qiita.com/takahiro_itazuri/items/d2bea1c643d7cca11352

### サンプルコード

```python
import numpy as np

sigmoid_range = 34.538776394910684

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -sigmoid_range, sigmoid_range)))

def derivative_sigmoid(o):
    return o * (1.0 - o)


# 3層ニューラルネットワーク
class ThreeLayerNetwork:
    # コンストラクタ
    def __init__(self, Xnodes, Ynodes, Znodes, lr):
        # 各レイヤーのノード数
        self.Xnodes = Xnodes
        self.Ynodes = Ynodes
        self.Znodes = Znodes

        # 学習率
        self.lr = lr

        # 重みの初期化(0~1の間の二次元行列)
        self.Wyx = np.random.normal(0.0, 1.0, (self.Ynodes, self.Xnodes))
        self.Wzy = np.random.normal(0.0, 1.0, (self.Znodes, self.Ynodes))

        # 活性化関数
        self.af = sigmoid
        self.daf = derivative_sigmoid

    # 誤差逆伝搬(引数は横一列のベクトル、Trowは答えの縦ベクトル)
    def backprop(self, Xrow, Trow):
        # 縦ベクトルに変換
        Xout = np.array(Xrow, ndmin=2).T
        Zteach = np.array(Trow, ndmin=2).T

        # 隠れ層
        Yin = np.dot(self.Wyx, Xout)    # Y = WX
        Yout = self.af(Yin)             # Y <= f_active(Y)

        # 出力層
        Zin = np.dot(self.Wzy, Yout)    # Z = WY
        Zout = self.af(Zin)             # Z <= f_active(Z)

        # YZ層の誤差逆伝搬
        dE_dZout = (Zout - Zteach)          # z×1行列：E = (1/2)(Zout-Zteach)^2
        dE_dZin = dE_dZout * self.daf(Zout) # z×1行列：Zout = f(Zin)
        dE_dWzy = np.dot(dE_dZin, Yout.T)   # z×1行列・1×y行列=>z×y行列：Zin = Wzy Yout
        self.Wzy -= self.lr * dE_dWzy       # 誤差の更新：W <- W - μ×(∂E/∂W)

        # XY層の誤差逆伝搬
        dE_dYout = np.dot(self.Wzy.T, dE_dZin)    # y×z行列・z×1行列 => y×1行列
        dE_dYin = dE_dYout * self.daf(Yout)       # y×1行列
        dE_dWyx = np.dot(dE_dYin, Xout.T)         # y×1行列・1×x行列 =>y×x行列
        self.Wyx -= self.lr * dE_dWyx             # 誤差の更新

    # 順伝搬
    def feedforward(self, idata):
        # 入力を縦ベクトルに変換
        Xout = np.array(idata, ndmin=2).T  # x×1行列

        # 隠れ層(Y = f(WX))
        Yin = np.dot(self.Wyx, Xout)    # y×x行列・x×1行列=> y×1行列
        Yout = self.af(Yin)             # y×1行列

        # 出力層
        Zin = np.dot(self.Wzy, Yout)    # z×y行列・y×1行列=> z×1行列
        Zout = self.af(Zin)             # z×1行列

        return Zout

```

あくまで学習用ですので、実用の際はライブラリを使用する方が速度面でも利便性でも勝ります

## 畳み込みニューラルネットワーク(CNN)

基本的に TensorFlow の公式チュートリアルをコピペしてコメントを追加しただけです

https://www.tensorflow.org/tutorials/images/cnn?hl=ja

Convolution に必要な層は例外処理が大変なため numpy のみ実装はまた今度に

```python
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
```

Conv2D で畳み込みして特徴を抽出。サンプルでは 3×3 フィルタを使用し、32->64->64 個のノード数に推移している

画素数が多いので、途中で MaxPooling2D を使用して最大値のみを取得するようにダウンサイジングをしている

前半と後半で層のノードの意味が異なり、Flatten()で一列のノード群にし NN を後半で実行している

この例では relu と softmax を使用しているが、sigmoid なども使用可能

## Recurrent Neural Network(RNN)

ある系列データ X と Y の規則性を求めるのに使用

例えば

x = [1, 3, 5, 6, 7, 9, ... ,Xi]

y = [1, 4, 9,15,21,30, ... ,Yi]

というデータがある場合

Yi = ∑Xi

と推測できる。機械にはこの変換式が与えられていない状況で規則性を予測したい

### サンプルコード

```python
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
model.add(layers.SimpleRNN(output_dim, activation=None,input_shape=(None, input_dim), return_sequences=True))

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
```

### 実行結果

```
⭐️学習結果⭐️
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
[ 0.9999999  1.9999998  2.9999995  3.9999995  4.9999995  5.9999995
  6.9999995  7.9999995  8.999999   9.999999  10.999999  11.999999
 12.999999  13.999999  14.999999  15.999999  16.999998  17.999998
 18.999998  19.999998 ]
```

Yi = ∑Xi が与えられなくても結びつきを予想し、さらに未来も推定できていることがわかる

それにしても、RNN 層を一行でかけるので、巨人の肩に乗ることの偉大さを痛感します

## 敵対敵生成ネットワーク (GAN)

ある「動物を表す画像」が与えられた時、それを「猫」と判定する場合は DNN を用いれば OK

しかし逆に、「猫」を入力として「猫の画像」を出力するモデルを生成する場合に GAN を用いる

### サンプルコード

```python
# 敵対敵生成ネットワーク
# 勉強用に以下の記事からコピペしたものとなります
# https://qiita.com/triwave33/items/1890ccc71fab6cbca87e

from __future__ import print_function, division

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Reshape, Flatten, Dropout
from tensorflow.keras.layers import BatchNormalization, Activation, ZeroPadding2D
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import UpSampling2D, Conv2D
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam

import matplotlib.pyplot as plt
import numpy as np


class GAN():
    def __init__(self):
        # mnistデータ用の入力データサイズ
        self.img_rows = 28
        self.img_cols = 28
        self.channels = 1
        self.img_shape = (self.img_rows, self.img_cols, self.channels)

        # その他の変数
        self.z_dim = 100                # 潜在変数の次元数
        optimizer = Adam(0.0002, 0.5)   # オプティマイザー

        # discriminatorモデル
        self.discriminator = self.__build_discriminator()
        self.discriminator.compile(loss='binary_crossentropy',
                                   optimizer=optimizer,
                                   metrics=['accuracy'])

        # Generatorモデル
        self.generator = self.__build_generator()  # generatorは単体で学習しないのでコンパイルは必要ない

        # 生成器と判別器を合体
        self.combined = self.__build_combined()
        self.combined.compile(loss='binary_crossentropy', optimizer=optimizer)

    # 生成器
    def __build_generator(self):

        noise_shape = (self.z_dim,)

        model = Sequential()
        model.add(Dense(256, input_shape=noise_shape))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(1024))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(np.prod(self.img_shape), activation='tanh'))
        model.add(Reshape(self.img_shape))

        model.summary()

        return model

    # 判別器
    def __build_discriminator(self):

        img_shape = (self.img_rows, self.img_cols, self.channels)

        model = Sequential()
        model.add(Flatten(input_shape=img_shape))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(256))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1, activation='sigmoid'))

        model.summary()

        return model

    def __build_combined(self):
        self.discriminator.trainable = False
        model = Sequential([self.generator, self.discriminator])
        return model

    # 学習
    def train(self, epochs, batch_size=128, save_interval=50):

        # mnistデータの読み込み
        (X_train, _), (_, _) = mnist.load_data()

        # 値を-1 to 1に規格化
        X_train = (X_train.astype(np.float32) - 127.5) / 127.5
        X_train = np.expand_dims(X_train, axis=3)

        half_batch = int(batch_size / 2)

        for epoch in range(epochs):

            # ---------------------
            #  Discriminatorの学習
            # ---------------------
            # バッチサイズの半数をGeneratorから生成
            noise = np.random.normal(0, 1, (half_batch, self.z_dim))
            gen_imgs = self.generator.predict(noise)

            # バッチサイズの半数を教師データからピックアップ
            idx = np.random.randint(0, X_train.shape[0], half_batch)
            imgs = X_train[idx]

            # discriminatorを学習
            # 本物データと偽物データは別々に学習させる
            d_loss_real = self.discriminator.train_on_batch(
                imgs, np.ones((half_batch, 1)))
            d_loss_fake = self.discriminator.train_on_batch(
                gen_imgs, np.zeros((half_batch, 1)))
            # それぞれの損失関数を平均
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            # ---------------------
            #  Generatorの学習
            # ---------------------
            noise = np.random.normal(0, 1, (batch_size, self.z_dim))

            # 生成データの正解ラベルは本物（1）
            valid_y = np.array([1] * batch_size)

            # Train the generator
            g_loss = self.combined.train_on_batch(noise, valid_y)

            # 進捗の表示
            print("%d [D loss: %f, acc.: %.2f%%] [G loss: %f]" %
                  (epoch, d_loss[0], 100*d_loss[1], g_loss))

            # 指定した間隔で生成画像を保存
            if epoch % save_interval == 0:
                self.save_imgs(epoch)

    # 画像を保存
    def save_imgs(self, epoch):
        # row,col
        r, c = 5, 5

        noise = np.random.normal(0, 1, (r * c, self.z_dim))
        gen_imgs = self.generator.predict(noise)

        # rescale [-1, 1] to [0, 1]
        gen_imgs = 0.5 * gen_imgs + 0.5

        fig, axs = plt.subplots(r, c)
        cnt = 0
        for i in range(r):
            for j in range(c):
                axs[i, j].imshow(gen_imgs[cnt, :, :, 0], cmap='gray')
                axs[i, j].axis('off')
                cnt += 1
        fig.savefig("images/mnist_%d.png" % epoch)
        plt.close()


if __name__ == '__main__':
    gan = GAN()
    gan.train(epochs=30000, batch_size=32, save_interval=100)

```

### 実行結果
