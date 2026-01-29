明白了，我幫你整理成一篇適合小學6年級學生看的 Python 筆記，用簡單易懂的方式，把今天上課的內容都整理好了📒✨

---

# 🐍 Python 小筆記（6年級版）

## 1️⃣ 比較運算子

用來比大小或判斷相等的符號，只能比相同種類的東西（像數字比數字，字串比字串）：

- `==`：等於
- `!=`：不等於
- `>`、`<`：大於、小於
- `>=`、`<=`：大於等於、小於等於

---

## 2️⃣ 算數指定運算子

可以簡單修改變數的數值：

```python
a = 1
a += 1  # a = a + 1
a -= 1  # a = a - 1
a *= 2  # a = a * 2
a /= 2  # a = a / 2
a //= 2 # 取整數除法
a %= 2  # 取餘數
a **= 2 # 次方
```

---

## 3️⃣ 計算順序（很重要⚡️）

1. `()` 括號
2. `**` 次方
3. `* / // %` 乘除、取商、取餘數
4. `+ -` 加減
5. 比較運算子 `== != > < >= <=`
6. `not`
7. `and`
8. `or`
9. `=`、`+=`、`-=`、`*=`…（算數指定運算子）

---

## 4️⃣ while 迴圈

只要條件是 True，就會一直做：

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

- `break`：可以跳出迴圈

```python
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
```

---

## 5️⃣ 隨機數字

先匯入 random 模組：

```python
import random

# 跟 range 一樣設定範圍
random.randrange(7)    # 0~6
random.randrange(1,6)  # 1~5
random.randrange(1,6,2)# 1,3,5

# randint 會包含結束數字
random.randint(1,6)    # 1~6
```

---

## 6️⃣ 猜數字遊戲

```python
answer = random.randrange(1,101)

while True:
    a = int(input("請輸入數字: "))
    if a > answer:
        print("太大了")
    elif a < answer:
        print("太小了")
    else:
        print("猜對了!")
        break
```

---

## 7️⃣ Streamlit 顯示圖片

```python
import streamlit as st
import os

st.title("圖片元件")
st.image("image/apple.png", width=300)

# 顯示資料夾裡的所有圖片
image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

# 使用者輸入大小
image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)

st.success("購買成功!")
```

---

## 8️⃣ 字典（dict）

用 `key: value` 存資料，key 唯一，value 可以重複：

```python
d = {"a":1, "b":2, "c":3}

# 取得 key、value
d.keys()   # 所有 key
d.values() # 所有 value
d.items()  # key 與 value

# 新增/修改
d["d"] = 4
d["a"] = 5

# 刪除
d.pop("a")  # 刪掉 key "a"

# 檢查
"a" in d
"e" in d
```

- 可以存複雜資料：

```python
d = {"a":[1,2,3], "b":{"c":4,"d":5}}
print(d["a"][0])  # 1
print(d["b"]["c"]) # 4
```

- 成績系統：

```python
grade = {
    "小明":{"國文":[90,80,70],"數學":[85,75,65],"英文":[95,85,75]},
    "小美":{"國文":[88,78,68],"數學":[83,73,63],"英文":[93,83,73]},
    "小華":{"國文":[86,76,66],"數學":[81,71,61],"英文":[91,81,71]}
}

# 計算總平均
for name, subjects in grade.items():
    total = 0
    for scores in subjects.values():
        total += sum(scores)
    avg = total / (len(subjects)*3)
    print(f"{name}的總平均成績是{avg:.2f}")
```

---

## 9️⃣ 函數（function）

- 定義函數用 `def`

```python
def hello():
    print("Hello World")
```

- 函數有參數

```python
def hello(name):
    print(f"Hello, {name}!")
```

- 函數有回傳值

```python
def add(a,b):
    return a+b
sum = add(3,4)
```

- 多個回傳值

```python
def add_sub(a,b):
    return a+b, a-b
sum, sub = add_sub(5,6)
```

- 預設參數

```python
def hello(name, message="Hello"):
    print(f"{message}, {name}!")
```

- 限制參數型態

```python
def add(a: int, b: int = 0) -> int:
    return a+b
```

---

這樣整理下來，小學6年級的同學應該也可以慢慢看懂每個指令在幹嘛了✨
如果你要，我可以幫你畫一張**圖解版本的 Python 筆記**，用圖表示迴圈、函數、字典，會更容易記住📊

你要我幫你做嗎，我的 lord？
