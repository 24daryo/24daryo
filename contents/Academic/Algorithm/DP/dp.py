import numpy as np


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

    # 遷移を表示(デバッグ用)
    for y in range(N+1):
        # break
        print(dp[y])

    return max_value


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
