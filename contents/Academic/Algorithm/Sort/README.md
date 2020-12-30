# ソートアルゴリズム

## 概要

学習用にまとめたコード集です。実際は実行速度の観点から言語標準のソート関数の使用をお勧めします。

## 一覧

### バブルソート

安定なソート
オーダー：O(n^2)

```python:bubble.py
def sort(array: list) -> list:
    size = len(array)
    for i in range(size):
        for j in range(i, size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
```

### 挿入ソート

```python:selection.py
# 挿入ソート
def sort(array):
    size = len(array)

    for i in range(1, size):
        target = array[i]
        blank = i

        # 対象より大きいものは右方向にシフトする。同時に空欄位置も取得する
        while blank >= 1 and target < array[blank-1]:
            array[blank] = array[blank-1]
            blank -= 1

        # シフト後の空スペースに挿入
        array[blank] = target
    return array
```

### 選択ソート

```python:selection.py
def sort(array):
    size = len(array)
    for i in range(size):
        # 最小要素の場所を取得する
        min_id = i
        for j in range(i, size):
            if array[j] < array[min_id]:
                min_id = j
        # 要素を交換する
        array[i], array[min_id] = array[min_id], array[i]
    return array
```

### マージソート

```python:merge.py
def sort(array) -> list:
    size = len(array)

    if size <= 1:
        return array
    else:
        # 半分の位置を求める
        mid = int(size / 2)

        # リストを左右に分割する(再帰処理)
        left = sort(array[:mid])
        right = sort(array[mid:])

        # 出力用の配列を作成
        output = []

        # 左右のリストから小さい順に取り出す
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))

        # 残った左右どちらかのリストを出力に結合する
        if len(left) != 0:  # 左が残った
            output += left
        elif len(right) != 0:  # 右が残った
            output += right

        return output
```

### クイックソート

```python:quick.py
import statistics

def sort(array) -> list:

    # 要素数が１ならそのままリターンする
    if len(array) <= 1:
        return array

    # 振り分ける基準値を取得(今回はメジアン)
    pivot = int(statistics.median(array))

    # 基準値に従い、配列を振り分ける
    left = []
    mid = []
    right = []
    for element in array:
        if element < pivot:  # 基準より小さいものは左へ
            left.append(element)
        elif element > pivot:  # 基準より大きいものは右へ
            right.append(element)
        else:  # 基準と等しいものは真ん中へ
            mid.append(element)

    # 左右はソートされていると限らないので、再帰的にソートさせる
    left = sort(left)
    right = sort(right)

    # リストを結合して出力
    return left + mid + right

```

### シェルソート

```python:shell.py
def sort(array):
    h = len(array) // 2

    while h > 0:
        # h間隔の挿入ソート
        size = len(array)
        for i in range(h, size):
            target = array[i]
            left = i
            while left >= h and target < array[left - h]:
                array[left] = array[left - h]
                left -= h
            array[left] = target
        h //= 2
    return array
```

### バケットソート

```python:bucket.py
# バケットソート(制約：0以上の整数配列でのみ使用可能)
def sort(array) -> list:
    # 最大要素をバケットのサイズとする
    size = max(array) + 1

    # バケットを初期化する
    buckets = list()
    for i in range(size):
        buckets.append(False)

    # 対応するバケットに要素を追加する
    for element in array:
        index = element
        buckets[index] = True

    # 空の要素を取り除く
    output = list()
    for i in range(size):
        if buckets[i] == True:
            output.append(i)

    return output
```

## ソートの実行時間比較

### 要素数 = 1,000

```
⭐️実行時間計測⭐️
バブルソート　：  50.09ms
挿入ソート　　：  39.13ms
選択ソート　　：  29.56ms
マージソート　：   3.85ms
クイックソート：   2.22ms
シェルソート　：   2.36ms
バケットソート：   0.21ms
```

クイックソートよりシェルソートの方が速い！

### 要素数 = 10,000

```
⭐️実行時間計測⭐️
バブルソート　：4399.93ms
挿入ソート　　：4228.87ms
選択ソート　　：2908.84ms
マージソート　：  52.14ms
シェルソート　：  39.57ms
クイックソート：  30.57ms
バケットソート：   2.01ms
```

### 要素数 = 100,000

```
⭐️実行時間計測⭐️
マージソート　：1220.16ms
シェルソート　： 640.02ms
クイックソート： 433.45ms
バケットソート：  23.09ms
```

### 要素数 = 1,000,000

```
⭐️実行時間計測⭐️
シェルソート　：10941.79ms
クイックソート：5909.53ms
バケットソート： 365.84ms
```

制約なしならクイックソートが一番速い！
空間計算量が許すならバケットソートが強い！
