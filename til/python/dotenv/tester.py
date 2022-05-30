import os

from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

item = os.getenv('TEST_ENV')
if item:
    print("成功")
    print("TEST_ENV：" + item)
else:
    print("失敗")
    print(item)
