import random


def liner_serch(array, target):
    for i, element in enumerate(array):
        if element == target:
            print("{0}番目に{1}が存在します".format(i+1, target))
            return
    print("{0}が見つかりませんでした".format(target))
    return


def shuffle(array: list) -> list:
    size = len(array)
    for i in range(size):
        rnd = random.randint(0, size-1)
        array[i], array[rnd] = array[rnd], array[i]
    return array


array = [i for i in range(10)]
array = shuffle(array)
print(array)
liner_serch(array, 8)
