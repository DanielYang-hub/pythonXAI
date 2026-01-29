import streamlit as st
import time

st.title("購物平台")

# ---------------- 欄位數量輸入框 ----------------
欄位數量 = st.number_input("請輸入欄位數量", min_value=1, step=1)

# 初始化商品資料
if "products" not in st.session_state:
    st.session_state.products = {
        "apple": {"price": 10, "stock": 10, "img": "image/apple.png", "last_bought": 0},
        "banana": {
            "price": 10,
            "stock": 10,
            "img": "image/banana.png",
            "last_bought": 0,
        },
        "b師": {"price": 10, "stock": 10, "img": "image/bg.png", "last_bought": 0},
        "orange": {
            "price": 10,
            "stock": 10,
            "img": "image/orange.png",
            "last_bought": 0,
        },
    }

# 追蹤新增庫存最後一次時間
if "last_added" not in st.session_state:
    st.session_state.last_added = 0
if "last_added_product" not in st.session_state:
    st.session_state.last_added_product = ""

# ---------------- 商品顯示與購買 ----------------
products = list(st.session_state.products.items())

# 將商品分批到指定欄位數
for start in range(0, len(products), 欄位數量):
    cols = st.columns(欄位數量)
    for i, (name, info) in enumerate(products[start : start + 欄位數量]):
        with cols[i]:
            st.image(info["img"], width=150)
            st.markdown(f"### **{name}**")
            st.write(f"Price: {info['price']} 元")
            st.write(f"Stock: {info['stock']} 個")

            # 購買按鈕
            if st.button(f"購買 {name}", key=f"btn_{name}"):
                buy_qty = st.number_input(
                    f"購買數量 {name}", min_value=1, step=1, key=f"qty_{name}"
                )
                if info["stock"] > 0:
                    qty = min(buy_qty, info["stock"])
                    st.session_state.products[name]["stock"] -= qty
                    st.session_state.products[name]["last_bought"] = time.time()

            # 購買成功訊息 3 秒
            if time.time() - info["last_bought"] <= 3:
                st.success("購買成功")

# ---------------- 新增商品庫存 ----------------
st.markdown("---")
st.subheader("新增商品庫存")

col1, col2 = st.columns([2, 1])

with col1:
    new_product = st.selectbox("請選擇商品名稱", list(st.session_state.products.keys()))

with col2:
    add_quantity = st.number_input("數量", min_value=1, step=1)

if st.button("新增庫存"):
    st.session_state.products[new_product]["stock"] += add_quantity
    st.session_state.last_added = time.time()
    st.session_state.last_added_product = new_product

# 新增庫存成功訊息 3 秒
if (
    time.time() - st.session_state.last_added <= 3
    and st.session_state.last_added_product
):
    st.success(f"{st.session_state.last_added_product} 庫存新增成功！ +{add_quantity}")

# ---------------- 顯示目前商品庫存 ----------------
st.subheader("目前商品庫存")
for name, info in st.session_state.products.items():
    st.write(f"{name}: {info['stock']} 個")
