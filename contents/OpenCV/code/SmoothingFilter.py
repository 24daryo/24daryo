import cv2
import numpy as np

# パスを指定
path = "../image/sample.png"

# 画像を読み込み
img = cv2.imread(path)

# 画像を表示
cv2.imshow('img', img)
cv2.waitKey(0)

# img が入力

# カーネルを生成
kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

copy = cv2.filter2D(img, -1, kernel)

cv2.imshow('img2', copy)
cv2.waitKey(0)
cv2.imwrite('../image/save.png', copy)
