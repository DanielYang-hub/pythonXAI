# 比較運算子能同樣類型作比較
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True


# 邏輯運算子
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or 運算子,只要有一個條件為 True,結果就是 True
print(True or True)  # True
print(True or False)  # False
print(False or True)  # True
print(False or False)  # False

# not 運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. o

# 密碼門檢查
password = input("請輸入密碼：")
if password == "1234":
    print("密碼正確，歡迎Daniel進入系統！")
elif password == "5678":
    print("密碼正確，歡迎Joseph進入系統！")
elif password == "0000":
    print("密碼正確，歡迎Toby進入系統！")
else:
    print("密碼錯誤，請重新輸入！")
# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件,所以縮短判斷條件的複雜度也節省了時間
# 但是如果使用多個if來做獨立判斷,則每個if都會被執行所以效率較低
