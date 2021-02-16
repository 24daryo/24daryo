#　コードのコメントルール

# コメントをつけるとき
# ①アルゴリズムを使用したとき
# Using quick sort for performance gains

# ②タグ付けを使用する(この三つは特定のキーワード)
# TODO: Add condition for when val is None
# BUG:
# FIXME:


# 型の指定も積極的に付帯させる
def hello_name(name: str) -> str:
    return(f"Hello {name}")


def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")

# 基本的には


def say_hello_detail(name):
    """This is the summary line

    This is the further elaboration of the docstring. Within this section,
    you can elaborate further on details as appropriate for the situation.
    Notice that the summary and the elaboration is separated by a blank new
    line.
    """

    print(f"Hello {name}, is it me you're looking for?")
