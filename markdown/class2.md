---
Python & Streamlit 課程筆記 🐍💻

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
