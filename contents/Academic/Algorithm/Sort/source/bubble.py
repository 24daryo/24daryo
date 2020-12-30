import Utility as U


# バブルソート
def sort(array: list) -> list:
    size = len(array)
    for i in range(size):
        for j in range(i, size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


print("⭐️バブルソート⭐️")

array = U.SetArray(20)
print("配列を初期化")
print(array)

array = U.Shuffle(array)
print("シャッフル")
print(array)

array = sort(array)
print("ソート後")
print(array)
