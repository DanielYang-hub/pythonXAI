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
