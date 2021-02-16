import logging

from abc import ABCMeta, abstractmethod
import numpy


class Vector(metaclass=ABCMeta):
    """本システムを使用するアカウントユーザーを示すクラスです。

    :param name: ユーザーのアカウント名
    :param user_type：アカウントのタイプ（adminかnormal）

    :Example:

    >>> import User
    >>> taro = User("taro", "admin")
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        logging.info('Vector 2D (%s,%s)', x, y)

    # @abstractmethod
    def dot(self):
        pass

    # @staticmethod
    # @abstractmethod
    def zero(self):
        print("super")
        pass

    @abstractmethod
    def __repr__(self):  # printなどで使用可能にする
        pass


class Vector2(Vector):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        logging.info('Init Vector2(%s,%s)', x, y)

    @property
    @staticmethod
    def zero():
        """return Vector2(0, 0)"""

        print("test")
        return Vector2(0, 0)

    @property
    def internal(self):
        pass

    def __repr__(self):  # eval関数でオブジェクトを復元可能な表現
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    a = Vector2(1, 2)
    z = Vector2.zero
    p = Vector2(1, 4)
    print(z)
    print(p)
    #c = Vector2(0, 0).internal()
