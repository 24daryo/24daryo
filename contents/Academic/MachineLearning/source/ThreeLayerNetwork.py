import numpy as np

# ほとんど以下の記事を参考にしました
# https://qiita.com/takahiro_itazuri/items/d2bea1c643d7cca11352
# 個人的にわかりやすいように変数名を割り当て、コメントを追加しました
sigmoid_range = 34.538776394910684


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -sigmoid_range, sigmoid_range)))


# ベクトル演算にも対応
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
        dE_dZout = (Zout - Zteach)         # z×1行列：E = (1/2)(Zout-Zteach)^2
        dE_dZin = dE_dZout * self.daf(Zout)  # z×1行列：Zout = f(Zin)
        dE_dWzy = np.dot(dE_dZin, Yout.T)  # z×1行列・1×y行列=>z×y行列：Zin = Wzy Yout
        self.Wzy -= self.lr * dE_dWzy      # 誤差の更新：W <- W - μ×(∂E/∂W)

        # XY層の誤差逆伝搬
        dE_dYout = np.dot(self.Wzy.T, dE_dZin)    # y×z行列・z×1行列 => y×1行列
        dE_dYin = dE_dYout * self.daf(Yout)       # y×1行列
        dE_dWyx = np.dot(dE_dYin, Xout.T)         # y×1行列・1×x行列 =>y×x行列
        self.Wyx -= self.lr * dE_dWyx            # 誤差の更新

    # 順伝搬(入力データから結果を取得、入力は横一列のベクトル)
    def feedforward(self, idata):
        # 入力を縦ベクトルに変換
        # idata = [0.15 0.21 0.33] => o_i = [[0.15]
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


def main(inData, outData):
    # パラメータ
    xSize = len(inData[0])
    ySize = 3
    zSize = len(outData[0])
    lr = 0.4

    # ニューラルネットワークの初期化
    nn = ThreeLayerNetwork(xSize, ySize, zSize, lr)

    # 学習
    epoch = 100
    for e in range(epoch):
        print('epoch回数：', e)
        data_size = len(inData)
        for i in range(data_size):
            if i % 1000 == 0:
                print('  train: {0:>5d} / {1:>5d}'.format(i, data_size))
            idata = inData[i]
            tdata = outData[i]
            nn.backprop(idata, tdata)

    # テスト
    print("0を入力するとき")
    sample = np.array([
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
    ]).flatten()
    sample_result = nn.feedforward(sample)
    print(sample_result)
    print("1を入力するとき")
    sample = np.array([
        [0, 1, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1],
    ]).flatten()
    sample_result = nn.feedforward(sample)
    print(sample_result)

    '''
    scoreboard = []
    for record in test_data_list:
        val = record.split(',')
        idata = (np.asfarray(val[1:]) / 255.0 * 0.99) + 0.01
        tlabel = int(val[0])
        predict = nn.feedforward(idata)
        plabel = np.argmax(predict)
        scoreboard.append(tlabel == plabel)
        pass

    scoreboard_array = np.asarray(scoreboard)
    print('performance: ', scoreboard_array.sum() / scoreboard_array.size)
    '''


training_data = [
    {
        "input": np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
        ]),
        "output":np.array([1, 0])
    },
    {
        "input": np.array([
            [0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
        ]),
        "output":np.array([1, 0])
    },
    {
        "input": np.array([
            [0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
        ]),
        "output":np.array([1, 0])
    },
    {
        "input": np.array([
            [0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
        ]),
        "output":np.array([1, 0])
    },
    {
        "input": np.array([
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0],
        ]),
        "output":np.array([1, 0])
    },
    {
        "input": np.array([
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1],
        ]),
        "output":np.array([0, 1])
    },
    {
        "input": np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]),
        "output":np.array([0, 1])
    },
    {
        "input": np.array([
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
        ]),
        "output":np.array([0, 1])
    },
    {
        "input": np.array([
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
        ]),
        "output":np.array([0, 1])
    },
    {
        "input": np.array([
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1],
        ]),
        "output":np.array([0, 1])
    },
]

inData = []
outData = []
for item in training_data:
    inData.append(item["input"].flatten())
    outData.append(item["output"])

main(inData, outData)
