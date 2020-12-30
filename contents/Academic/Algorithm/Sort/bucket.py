import Utility as U


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


print("【バケットソート】")

array = U.SetArray(20)
print("配列を初期化")
print(array)

array = U.Shuffle(array)
print("シャッフル後")
print(array)

array = sort(array)
print("ソート後")
print(array)
