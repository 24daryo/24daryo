# ソートアルゴリズム

## 概要

学習用にまとめたコード集です。実際は実行速度の観点から言語標準のサーチ関数の使用をお勧めします。

## 一覧

### 線形探索

端から順に要素をチェック。o(n)。

```python
def liner_serch(array, target):
    for i, element in enumerate(array):
        if element == target:
            print("{0}番目に{1}が存在します".format(i+1, target))
            return
    print("{0}が見つかりませんでした".format(target))
    return
```

### 二分探索

範囲を絞り込みながらチェック。o(logn)。元から整列されていないと使用できない。

```python
def binary_serch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            print("{0}番目に{1}が存在します".format(mid, target))
            return
        elif target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1

    print("{0}が見つかりませんでした".format(target))
    return
```

### ハッシュ法

##　実行時間比較

## 終わりに
