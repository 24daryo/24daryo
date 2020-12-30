import random


# ソート済みを前提とする
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


def shuffle(array: list) -> list:
    size = len(array)
    for i in range(size):
        rnd = random.randint(0, size-1)
        array[i], array[rnd] = array[rnd], array[i]
    return array


array = [i for i in range(20)]
array = shuffle(array)
print(array)
binary_serch(array, 8)
