from concurrent.futures import ThreadPoolExecutor
import time


def func1():
    while True:
        time.sleep(1)
        print("func1")


def func2():
    while True:
        time.sleep(3)
        print("func2")


if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        feature = executor.submit(func1)
        feature = executor.submit(func2)
