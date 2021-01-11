# 機械学習の実装

## 【基本事項】

### ３層構造ニューラルネットワーク

入力層 X、中間層 Y、出力層 Z で構成されたネットワーク
学習用のため numpy のみで実装されている
ほとんど以下の記事を参考にしました

https://qiita.com/takahiro_itazuri/items/d2bea1c643d7cca11352

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
        # 例
        # W = [[0.23 0.56 0.72]     X =[[0.15]      Y= [[0.67]
        #      [0.83 0.38 0.52]         [0.21]          [0.39]
        #      [0.73 0.55 0.02]         [0.33]]         [0.88]
        #      [0.95 0.73 0.28]]                        [0.27]]
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

        # YZ層の誤差逆伝搬(∂E/∂Wzy = (∂E/∂Zout)・(∂Zout/∂Zin)・(∂Zin/∂Wzy))
        dE_dZout = (Zout - Zteach)          # z×1行列：E = (1/2)(Zout-Zteach)^2
        dE_dZin = dE_dZout * self.daf(Zout) # z×1行列：Zout = f(Zin)
        dE_dWzy = np.dot(dE_dZin, Yout.T)   # z×1行列・1×y行列=>z×y行列：Zin = Wzy Yout
        self.Wzy -= self.lr * dE_dWzy       # 誤差の更新：W <- W - μ×(∂E/∂W)

        # XY層の誤差逆伝搬
        dE_dYout = np.dot(self.Wzy.T, dE_dZin)    # y×z行列・z×1行列 => y×1行列
        dE_dYin = dE_dYout * self.daf(Yout)       # y×1行列
        dE_dWyx = np.dot(dE_dYin, Xout.T)         # y×1行列・1×x行列 =>y×x行列
        self.Wyx -= self.lr * dE_dWyx             # 誤差の更新

    # 順伝搬(入力データから結果を取得、入力は横一列のベクトル)
    def feedforward(self, idata):
        # 入力を縦ベクトルに変換
        # 例
        # idata = [0.15 0.21 0.33] => Xout = [[0.15]
        #                                    [0.21]
        #                                    [0.33]]
        Xout = np.array(idata, ndmin=2).T  # x×1行列

        # 隠れ層(Y = f(WX))
        # W = [[0.23 0.56 0.72]     X =[[0.15]      この場合Yは4行１列の行列
        #      [0.83 0.38 0.52]         [0.21]
        #      [0.73 0.55 0.02]         [0.33]]
        #      [0.95 0.73 0.28]]
        Yin = np.dot(self.Wyx, Xout)    # y×x行列・x×1行列=> y×1行列
        Yout = self.af(Yin)             # y×1行列

        # 出力層
        Zin = np.dot(self.Wzy, Yout)    # z×y行列・y×1行列=> z×1行列
        Zout = self.af(Zin)             # z×1行列

        return Zout

```

### 畳み込みニューラルネットワーク(CNN)

基本的に TensorFlow の公式チュートリアルをコピペしてコメントを追加しただけです

https://www.tensorflow.org/tutorials/images/cnn?hl=ja

Convolution に必要な層は例外処理が面倒だったので numpy のみ実装はまた今度

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
