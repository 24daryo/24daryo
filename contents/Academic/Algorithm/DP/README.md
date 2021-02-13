# 動的計画法

## 概要

学習用にまとめたコード集です。

### ナップザック問題

重さ w(i) と価値 v(i) がセットの宝が N 個 (0< i <= N) あり、重さ制限 c(0 < c)になるまで選んで持ち運べるときの最大価値は？

```python:selection.py
# ナップザック問題
# 重さの可能性を全て書き出し、一番価値ある値を出力
def knapsack(item, capacity):
    # アイテムの個数
    N = len(item)

    # DPの2次元配列を作成(-1は空値として扱う)
    dp = np.full((N+1, capacity+1), -1)

    # 初期化
    dp[0][0] = 0

    # DP(配列の要素は、ある重さのときの価値)
    for y in range(N):
        for x in range(capacity+1):
            # その重さでの価値の存在する場合のみ調べる
            if dp[y][x] >= 0:
                # ①追加しない場合：そのまま更新する
                dp[y+1][x] = dp[y][x]

                # ②追加をする場合：基準の重さを下回るなら追加
                value = item[y]["value"]
                weight = item[y]["weight"]
                next_weight = weight + x
                if next_weight <= capacity:
                    dp[y+1][next_weight] = dp[y][x] + value

    #　一番価値のある要素を取得
    max_value = dp[N].max()

    return max_value
```

実行例

```python
# 実行の様子
# リュックに積むことのできるアイテム
item = [
    {"value": 4, "weight": 7},
    {"value": 5, "weight": 8},
    {"value": 2, "weight": 4},
    {"value": 8, "weight": 12},
    {"value": 10, "weight": 11},
    {"value": 15, "weight": 13},
]

# 重さの制限
capacity = 20

# ナップザック問題の解
solution = knapsack(item, capacity)

# 表示
print(solution)
```

結果

```
追加の様子
[ 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1]
[ 0 -1 -1 -1 -1 -1 -1  4 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1]
[ 0 -1 -1 -1 -1 -1 -1  4  5 -1 -1 -1 -1 -1 -1  9 -1 -1 -1 -1 -1]
[ 0 -1 -1 -1  2 -1 -1  4  5 -1 -1  6  7 -1 -1  9 -1 -1 -1 11 -1]
[ 0 -1 -1 -1  2 -1 -1  4  5 -1 -1  6  7 -1 -1  9 10 -1 -1 11 13]
[ 0 -1 -1 -1  2 -1 -1  4  5 -1 -1  6  7 -1 -1  9 10 -1 14 11 13]
[ 0 -1 -1 -1  2 -1 -1  4  5 -1 -1  6  7 15 -1  9 10 17 14 11 13]
答え
17
```

# Coin Changing Problem

【問題】

額面が c1,c2,⋯,cm 円の m 種類のコインを使って n 円を支払うときのコインの最小の枚数を求めよ．
各額面のコインは何度でも使用できるとする．

【方針】

m 種類のコインを一つずつチェックし、0~n 円の範囲で条件を満たすかチェックする
計算量は O(mn)
