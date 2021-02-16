

class Test(object):
    """テスト用のクラス"""

    # クラス変数(静的動的に関わらず使用可能)
    prop_class = "class prop"

    def __init__(self):
        # インスタンス変数動的な場合のみ使用可能
        self.prop_instance = "instance prop"
        self.set_item = "set item"

        # 予め使用するinstance propはinitで宣言しておく

    def ver1(self):
        """通常のメソッド"""
        return "method"

    @staticmethod
    def ver2(*args):
        """staticメソッド

        使用上は変化ないが、参照は一つしかない
        """
        return "static method"

    @classmethod
    def ver3(cls, *args):
        """classメソッド"""
        return f"class method and {cls.prop_class}"

    @property
    def ver4(self):
        """property

        getしかできない、setしたい場合はver4にsettetを追加する
        """
        return "property"

    @ver4.setter
    def ver4(self, set_item):
        print(f"{set_item}をSetしました")
        self.set_item = set_item

    def instance_exapmle(self):
        """インタスタンス変数は初めに参照を明記して使用する"""

        myprop = self.prop_instance
        return myprop


# データコンテナンとしてのみの使用なら、以下のようにしてメモリ効率を図る
class Container(object):
    __slots__ = ['first_name', 'last_name']

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


if __name__ == "__main__":
    print(Test.prop_class)
    print(Test().prop_instance)
    print(Test().ver1())
    print(Test().ver2())
    print(Test.ver3())
    print(Test().ver4)

    a = Test()
    a.ver4 = "Hello World"
