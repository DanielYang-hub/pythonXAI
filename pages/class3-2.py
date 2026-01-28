import streamlit as st

# --- 重新整理按鈕 ---
if st.button("重新整理", key="refresh"):
    st.session_state.cart = []  # 清空購物籃
    st.rerun()  # 強制刷新畫面

st.title("點餐機")

# --- 初始化購物籃 ---
if "cart" not in st.session_state:
    st.session_state.cart = []

# --- 文字輸入 + 按鈕在同一行 ---
col1, col2 = st.columns([3, 1])

with col1:
    food_input_text = st.text_input("請輸入餐點", value="")
    st.session_state["food_input_text"] = food_input_text  # 儲存文字輸入

with col2:
    if st.button("加入", key="add_item"):
        food_input = st.session_state.get("food_input_text", "").strip()
        if food_input != "":
            st.session_state.cart.append(food_input)

# --- 顯示購物籃 ---
st.subheader("購物籃")

if st.session_state.cart:
    # 顯示每個項目 + 移除按鈕
    for i, item in enumerate(st.session_state.cart):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.write(f"{item}")  # 只顯示項目名稱
        with c2:
            if st.button("刪除", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()  # 按下移除後刷新畫面
