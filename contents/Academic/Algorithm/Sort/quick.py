import Utility as U
import statistics


# クイックソート
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


print("⭐️クイックソート⭐️")

array = U.SetArray(20)
print("配列を初期化")
print(array)

array = U.Shuffle(array)
print("シャッフル後")
print(array)

array = sort(array)
print("ソート後")
print(array)
