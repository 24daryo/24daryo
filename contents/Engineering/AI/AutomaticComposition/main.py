# 自動でコードを出力するRNNを実装してみる
from tensorflow.keras import models
from tensorflow.keras.layers import Dense, Activation, LSTM
from tensorflow.keras.optimizers import RMSprop
import numpy as np
import random
import sys

# 規則性を調べたいテキスト
text = "45364361"

# 全ての文字を重複なしで集計
chars = sorted(list(set(text)))
print('Total chars:', len(chars))

# 文字と数値の変換を生成
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

maxlen = 2  # 文字数
span = 2  # 文字を調べる間隔
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, span):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print("⭐️センテンス⭐️")
print(sentences)
print(next_chars)

# テキストのベクトル化
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

print("⭐️センテンス変換後⭐️")  # one-hotベクトルに変換
print(X)
print(y)

# モデルを定義する
model = models.Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


for iteration in range(1, 10):
    print()
    print('-' * 50)
    print('繰り返し回数: ', iteration)
    model.fit(X, y, batch_size=128, epochs=1)

    start_index = random.randint(0, len(text)-maxlen-1)

    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('-----diveristy', diversity)

        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('----- Seedを生成しました: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(40):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.

            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()
'''
x = [
    [["F"], ["G"], ["Em"]],
    [["C"], ["F"], ["G"]],
    [["Am"], ["F"], ["G"]]
]
y = [
    [["F"], ["G"], ["Em"], ["Am"]],
    [["C"], ["F"], ["G"], ["C"]],
    [["Am"], ["F"], ["G"], ["C"]]
]
x = [
    ["F", "G", "Em"],
    ["C", "F", "G"],
    ["Am", "F", "G"]
]
y = [
    ["F", "G", "Em", "Am"],
    ["C", "F", "G", "C"],
    ["Am", "F", "G", "C"]
]
'''
