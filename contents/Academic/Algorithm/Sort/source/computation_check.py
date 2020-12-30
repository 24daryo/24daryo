import bubble
import bucket
import insert
import merge
import quick
import selection
import shell

import Utility as U
import time

print("⭐️実行時間計測⭐️")
array = U.SetArray(10000)
array = U.Shuffle(array)

start = time.time()
arranged = bubble.sort(array)
elapsed_time = time.time() - start
elapsed_time *= 1000
print("バブルソート　：{:7.02f}ms".format(elapsed_time))

start = time.time()
arranged = selection.sort(array)
elapsed_time = time.time() - start
elapsed_time *= 1000
print("選択ソート　　：{:7.02f}ms".format(elapsed_time))

start = time.time()
arranged = merge.sort(array)
elapsed_time = time.time() - start
elapsed_time *= 1000
print("マージソート　：{:7.02f}ms".format(elapsed_time))

start = time.time()
arranged = quick.sort(array)
elapsed_time = time.time() - start
elapsed_time *= 1000
print("クイックソート：{:7.02f}ms".format(elapsed_time))

start = time.time()
arranged = shell.sort(array)
elapsed_time = time.time() - start
elapsed_time *= 1000
print("シェルソート　：{:7.02f}ms".format(elapsed_time))


start = time.time()
arranged = bucket.sort(array)
elapsed_time = time.time() - start
elapsed_time *= 1000
print("バケットソート：{:7.02f}ms".format(elapsed_time))

start = time.time()
arranged = insert.sort(array)
elapsed_time = time.time() - start
elapsed_time *= 1000
print("挿入ソート　　：{:7.02f}ms".format(elapsed_time))
