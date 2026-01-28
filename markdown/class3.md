Python & Streamlit 課程筆記 🐍💻

1️⃣ Streamlit 是什麼？

Streamlit 可以幫你做 網頁小程式，像做遊戲或小工具一樣。

import streamlit as st # 導入 Streamlit

st.title("我的小程式") # 顯示大標題
a = st.number_input("輸入一個數字", min_value=1, step=1) # 數字輸入框

st.title → 標題

st.number_input → 輸入數字

2️⃣ 印出圖形 🎨
2.1 數字金字塔
a = st.number_input("金字塔高度", min_value=1, step=1)
for i in range(1, a+1):
line = ""
for j in range(i):
line += str(i)
st.write(line)

✅ 會印出：

1
22
333
4444

外圈迴圈控制 列數

內圈迴圈控制 每列的數字

2.2 箭頭金字塔
n = st.number_input("箭頭層數", min_value=1, step=1)
a = ""
for i in range(1, n+1):
a += " "_(n-i) + "_"*(i*2-1) + "\n"
for i in range(n):
a += " "_(n-1) + "_" + "\n"
st.markdown(f"`\n{a}`")

✅ 會印出：

-

---

---

-
-

上半部 → 金字塔

下半部 → 箭頭杆

3️⃣ 列表 List 📋

列表可以存東西：

L = [1, 2, 3, "a", "b", "c"]
print(L[0]) # 第1個 = 1
print(L[3]) # 第4個 = "a"

3.1 切片 (取部分)
print(L[::2]) # 每2個取一次 → [1, 3, 'b']
print(L[1:4]) # 第2到第4個 → [2, 3, 'a']

3.2 加入或刪除
L.append("d") # 加到最後
L.remove("a") # 刪掉第一個 a
L.pop(0) # 刪掉第1個

3.3 遍歷
for item in L:
print(item)

4️⃣ 計算平均分數 📝
midterm = [80, 95, 78, 60, 55]
final = [64, 73, 52, 34, 95]

a = st.number_input("第幾位同學？", min_value=1, max_value=5, step=1)
average = (midterm[a-1] + final[a-1]) / 2
st.write(f"第{a}位同學平均 = {average}")

5️⃣ 欄位 Columns 🏗️

可以把網頁分成左右兩欄：

col1, col2 = st.columns([1,2])
col1.button("按鈕1")
col2.button("按鈕2")

[1,2] → 左邊小、右邊大

可以放文字、按鈕、輸入框

6️⃣ 文字輸入 ✏️
text = st.text_input("輸入文字", value="預設文字")
st.write(f"你輸入了: {text}")

7️⃣ 記住資料 Session State 💾

按下按鈕也不會忘記資料：

if "ans" not in st.session_state:
st.session_state.ans = 1

if st.button("加1"):
st.session_state.ans += 1

st.write(f"ans = {st.session_state.ans}")

8️⃣ 點餐小程式 🍔
if "cart" not in st.session_state:
st.session_state.cart = []

col1, col2 = st.columns([3,1])
with col1:
food_input = st.text_input("輸入餐點")
with col2:
if st.button("加入"):
if food_input.strip():
st.session_state.cart.append(food_input)

st.subheader("購物籃")
for i, item in enumerate(st.session*state.cart):
c1, c2 = st.columns([3,1])
with c1: st.write(item)
with c2:
if st.button("刪除", key=f"remove*{i}"):
st.session_state.cart.pop(i)
st.rerun()

輸入餐點 → 加入購物籃

可以刪除每個餐點

使用 Session State 保留資料
