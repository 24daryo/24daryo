# OpenCV(Python)を用いた実装

## 基本事項

### 画像の読み込み

```
# パスを指定
path = "../image/sample.png"

# 画像を読み込み
img = cv2.imread(path)
```

### 画素へのアクセス

```
# 画像の高さ、横幅、チャンネル数を取得
height, width, channels = img.shape[:3]

# 3重ループで直接画素にアクセス
for y in range(height):
    for x in range(width):
        for c in range(channels):
            img[y, x, c] = 100

# 重たい処理なので、何かしらの並列化が必要
```
