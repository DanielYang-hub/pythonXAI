import streamlit as st

with st.expander("Class1 課堂筆記"):
    st.write(
        """
             好～我幫你把今天學到的 **Python 指令** 整理成一份
👉 **「國小六年級也看得懂的筆記」**
用簡單的說法、搭配例子，當成複習小抄也很適合 ✨

---

## 🐍 Python 入門筆記（國小 6 年級版）

---

## 一、註解（給人看的說明）

📌 **註解** 是給「人」看的說明，電腦不會執行。

```python
# 這是單行註解
\"""
這是多行註解
\"""
```

👉 小技巧：
`Ctrl + ?` 可以快速註解或取消註解 👍

---

## 二、print()：顯示文字或數字

📌 `print()` 可以把內容顯示在螢幕上

```python
print("Hello World")
print(123)
```

---

## 三、基本資料型態（資料的種類）

| 型態  | 說明             | 例子         |
| ----- | ---------------- | ------------ |
| int   | 整數             | 1, 0, -5     |
| float | 小數             | 1.23, 3.14   |
| str   | 文字（字串）     | "apple"      |
| bool  | 布林值（對或錯） | True / False |

```python
print(1)
print(1.234)
print("apple")
print(True)
```

---

## 四、變數（幫資料取名字）

📌 **變數** 就像一個盒子，用來存東西

```python
a = 10
print(a)

a = "apple"
print(a)
```

👉 `=` 不是「等於」，是 **把右邊的東西存到左邊**

---

## 五、數學運算子（算數學）

| 符號 | 功能   |
| ---- | ------ |
| +    | 加     |
| -    | 減     |
| \*   | 乘     |
| /    | 除     |
| //   | 取商   |
| %    | 取餘數 |
| \*\* | 次方   |

```python
print(2 + 3)
print(2 ** 3)  # 2的3次方
```

### ✨ 運算優先順序

1. ()
2. \*\*
3. - / // %
4. - -

---

## 六、字串（文字）的玩法

```python
print("apple" + "pen")   # 文字相加
print("ha" * 3)          # 重複文字
```

---

## 七、f-string（把變數放進文字）

📌 用 `f""`，就能把變數放進 `{}` 裡

```python
name = "小明"
age = 12
print(f"我是{name}，今年{age}歲")
```

---

## 八、len() 與 type()

📌 `len()`：算長度
📌 `type()`：看資料型態

```python
print(len("apple"))     # 5
print(type(1))          # int
print(type("hi"))       # str
```

---

## 九、型態轉換（改變資料種類）

```python
int(1.2)        # 變整數
float(1)        # 變小數
str(123)        # 變文字
bool(1)         # 變 True
```

⚠️ 注意：

```python
int("hello")    # 會出錯！
```

---

## 十、input()：讓使用者輸入

📌 `input()` 讓使用者打字
⚠️ **輸入的內容一定是字串**

```python
a = input("請輸入數字")
print(int(a) + 10)
```

---

### ✏️ 小例子：算圓面積

```python
pi = 3.14
r = int(input("輸入半徑"))
area = pi * r ** 2
print(area)
```

### ✏️ 小例子：算 BMI

```python
cm = float(input("輸入身高")) / 100
kg = int(input("輸入體重"))
bmi = kg / (cm * cm)
print(bmi)
```

---

## 十一、比較運算子（比大小）

| 符號 | 意思     |
| ---- | -------- |
| ==   | 等於     |
| !=   | 不等於   |
| >    | 大於     |
| <    | 小於     |
| >=   | 大於等於 |
| <=   | 小於等於 |

```python
print(10 > 5)   # True
```

---

## 十二、邏輯運算子（想事情）

### and（而且）

```python
True and False  # False
```

### or（或者）

```python
True or False   # True
```

### not（相反）

```python
not True        # False
```

### ✨ 邏輯優先順序

1. ()
2. \*\*
3. - /
4. - -
5. 比較
6. not
7. and
8. or

---

## 十三、Streamlit（做網頁介面）

📌 Streamlit 可以把 Python 變成網頁

```python
import streamlit as st

st.title("這是標題")
st.write("顯示文字或數字")
st.text("只能顯示純文字")
```

### Markdown（漂亮文字）

```python
st.markdown(\"""
        # 大標題
        ## 小標題
        - 清單
        ** 粗體
        ** \""")
```

### 展開收合

```python
with st.expander("課堂筆記"):
    st.write("內容在這裡")
```

---

## ✅ 今天你學會了什麼？

✔ Python 基本指令
✔ 變數與運算
✔ 使用者輸入
✔ 判斷對或錯
✔ 用 Streamlit 做簡單網頁

"""
    )

with st.expander("Class2 課堂筆記"):
    st.write(
        """
---
# 🐍 Python 入門學習筆記（國小六年級版）

## 一、比較運算子（用來比大小、比一不一樣）

比較運算子是用來**比較兩個東西是不是一樣或誰比較大**，結果只會是：
👉 `True（對）` 或 `False（錯）`

| 運算子 | 意思       | 例子             |
| ------ | ---------- | ---------------- |
| `==`   | 等於       | `1 == 1` → True  |
| `!=`   | 不等於     | `1 != 1` → False |
| `>`    | 大於       | `3 > 2` → True   |
| `<`    | 小於       | `2 < 1` → False  |
| `>=`   | 大於或等於 | `1 >= 1` → True  |
| `<=`   | 小於或等於 | `1 <= 1` → True  |
---

## 二、邏輯運算子（判斷「而且 / 或是 / 相反」）

### 1️⃣ and（而且）

👉 **兩個都要對，才會是 True**

```python
True and True   → True
True and False  → False
```

### 2️⃣ or（或是）

👉 **只要有一個對，就是 True**

```python
True or False   → True
False or False  → False
```

### 3️⃣ not（相反）

👉 **把結果變相反**

```python
not True   → False
not False  → True
```

---

## 三、if / elif / else（如果…就…）

用來讓電腦「做選擇」。

### 📌 成績判斷例子（用 Streamlit）

```python
if number >= 90:
    顯示 A
elif number >= 80:
    顯示 B
elif number >= 70:
    顯示 C
elif number >= 60:
    顯示 D
else:
    顯示 F
```

👉 電腦會**從上面開始一個一個檢查**，
只要符合其中一個，就不會再往下看。

---

## 四、Streamlit 是什麼？（做網頁用的）

### ✨ 常用功能

- `st.number_input()`：讓使用者輸入數字
- `st.markdown()`：在網頁顯示文字
- `st.button()`：顯示按鈕
- `st.balloons()`：放氣球 🎈
- `st.snow()`：下雪 ❄️

### 📌 按鈕小例子

```python
if st.button("按我一下"):
    st.balloons()
```

👉 使用者一按，畫面就會放氣球！

---

## 五、奇數和偶數判斷（取餘數）

### `%` 是「取餘數」

- 除以 2 **沒有剩** → 偶數
- 除以 2 **有剩** → 奇數

```python
if number % 2 == 0:
    偶數
else:
    奇數
```

---

## 六、for 迴圈（一直重複做事情）

### 📌 基本寫法

```python
for i in range(5):
    print(i)
```

👉 會印出：`0 1 2 3 4`

### 📌 range 的用法

| 寫法            | 產生的數字 |
| --------------- | ---------- |
| `range(5)`      | 0,1,2,3,4  |
| `range(1,5)`    | 1,2,3,4    |
| `range(1,10,2)` | 1,3,5,7,9  |

---

## 七、數字金字塔（巢狀迴圈）

```python
for i in range(1, a+1):
    line = ""
    for j in range(i):
        line += str(i)
    顯示 line
```

👉 如果輸入 3，畫面會是：

```
1
22
333
```

---

## 八、input() 讓使用者輸入文字

```python
a = int(input("請輸入第一個數字:"))
b = int(input("請輸入第二個數字:"))
```

👉 `int()` 是把文字變成數字，不然不能算數學。

---

## 九、密碼檢查（多個 elif）

```python
if password == "1234":
    歡迎 Daniel
elif password == "5678":
    歡迎 Joseph
else:
    密碼錯誤
```

### ❗ 為什麼用 elif？

- `elif` 可以**避免重複檢查**
- 比用很多個 `if` **更快、更省力**

---

        """
    )
