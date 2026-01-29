import random

answer = random.randrange(1, 101)

while True:
    a = int(input("請輸入數字: "))

    if a > answer:
        print("太大了")
    elif a < answer:
        print("太小了")
    else:
        print("猜對了")
        break
