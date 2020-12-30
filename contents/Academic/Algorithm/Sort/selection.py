import Utility as U


# 選択ソート
# バブルソートより交換回数が少ないのが利点
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


print("⭐️選択ソート⭐️")

array = U.SetArray(20)
print("配列を初期化")
print(array)

array = U.Shuffle(array)
print("シャッフル")
print(array)

array = sort(array)
print("ソート後")
print(array)
