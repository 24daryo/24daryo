import random


def SetArray(size: int) -> list:
    array = []
    for i in range(size):
        array.append(i)
    return array


def Shuffle(array: list) -> list:
    size = len(array)
    for i in range(size):
        rnd = random.randint(0, size-1)
        array[i], array[rnd] = array[rnd], array[i]
    return array
