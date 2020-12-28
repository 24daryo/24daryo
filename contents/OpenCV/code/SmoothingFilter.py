import cv2

# パスを指定
path = "../image/sample.png"

# 画像を読み込み
img = cv2.imread(path)

# 画像を表示
cv2.imshow('img', img)
cv2.waitKey(0)


# 画素へのアクセス
height, width, channels = img.shape[:3]
for y in range(height):
    for x in range(width):
        for c in range(channels):
            img[y, x, c] = 100

cv2.imshow('img', img)
cv2.waitKey(0)
