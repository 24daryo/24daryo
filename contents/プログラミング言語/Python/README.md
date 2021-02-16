# Python での基本事項

自分なりに Python を使用する際に必要な項目をまとめたものとなります。

## 基本事項

### クラス設計

```Python main.py
class Vector:
    """本システムを使用するアカウントユーザーを示すクラスです。

    :param name: ユーザーのアカウント名
    :param user_type：アカウントのタイプ（adminかnormal）

    :Example:

    >>> import User
    >>> taro = User("taro", "admin")
    """
    def __init__(_x:float, _y:float):
        self.x = _x
        self.y = _y

if __name__ == "__main__":
    a = Vector():

```

### ユニットテスト

```Python
import unittest
import logging

def pow(x: float) -> float:
    return x*x

class UnitTest(unittest.TestCase):

    def test_pow(self):
        value = 3
        expected = 9
        actual = pow(value)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

```

### ログ

```Python
import logging

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    logger.info("この内容を保存します")

```

### デコレータ

### docstring

コメントをつけるとき

① アルゴリズムを使用したとき
Using quick sort for performance gains

② タグ付けを使用する(この三つは特定のキーワード)

```Python
# TODO: Add condition for when val is None
# BUG:
# FIXME:
```

型の指定も積極的に付帯させる

```Python
def hello_name(name: str) -> str:
    return(f"Hello {name}")
```

コメントは一行で簡潔にを心がける(PEP 257 参照)

```Python
def say_hello_bleaf(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
```

どうしても詳述する場合は、以下のように記述する。空行も重要。

```Python
def say_hello_detail(name):
    """This is the summary line

    This is the further elaboration of the docstring. Within this section,
    you can elaborate further on details as appropriate for the situation.
    Notice that the summary and the elaboration is separated by a blank new
    line.
    """

    print(f"Hello {name}, is it me you're looking for?")
```

また実際に使用する場合の例を「examples.py」として作成しておくと良い
Readme：プロジェクトとその目的の簡単な要約。
プロジェクトのインストールまたは運用に関する特別な要件を含める。

### 共同開発を考慮した記述

- オブジェクト指向設計
- ログ
- ユニットテスト
- デコレータ(@property, @staticmethod)
- `*args`、`**kwargs`の使用
- 例外処理
- docstring

```Python
import logging

import numpy

class Vector:
    """本システムを使用するアカウントユーザーを示すクラスです。

    :param name: ユーザーのアカウント名
    :param user_type：アカウントのタイプ（adminかnormal）

    :Example:

    >>> import User
    >>> taro = User("taro", "admin")
    """
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        logging.info('Vector 2D (%s,%s)', x, y)

    @abstractmethod
    def dot(self, *arges):
        pass


class Vector2(Vector):
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        logging.info('Vector 2D (%s,%s)', x, y)

```

## まとめ

以下の内容が共同開発に盛り込めるようにする

- オブジェクト指向設計
  - 条件文を増やす可能性が高い場合　=> class による継承
- ログ
  - 関数の実行順と時間計測を把握する場合に使用
- ユニットテスト
  - 予期せぬ値に備える。docstring にも記載する
- デコレータ(@property, @staticmethod)
  - 変数やクラスの役割を明記し、可読性を向上させる
- `*args`、`**kwargs`の使用
  - 予期せぬ値に対応する。「入力は寛容に、出力は厳格に」
- 例外処理
  - 必要に応じて try-catch を導入
- docstring
  - 開発者向けなら一行でシンプルに、様々な利用者を想定するなら詳細も記述
  - 詳細を記述する前に、もっとわかりやすい実装ができないか考慮する
  - バランスを考慮して、NumPy style docstrings を使用(人による)
