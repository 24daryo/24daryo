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
kernel = np.full((3, 3), 1/9)
kernel_y = len(kernel)
kernel_x = len(kernel[0])
N = int(kernel_y/2)
M = int(kernel_x/2)

# 5重ループにより畳み込み
H, W, channels = img.shape[:3]
copy = np.zeros((H, W, channels), np.uint8)
'''
for y in range(N, H-N):
    for x in range(M, W-M):
        for c in range(channels):
            for py in range(-N, N+1):
                for px in range(-M, M+1):
                    copy[y, x, c] += img[y+py, x+px, c] * kernel[py+N, px+M]
img = copy
'''
copy = cv2.filter2D(img, -1, kernel)

cv2.imshow('img2', copy)
cv2.waitKey(0)
