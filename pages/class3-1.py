import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2columns
col1.button("按鈕1", key="btn1")  # 在col1中建立一個按紐類似st.button("按鈕1")
col2.button("按鈕2", key="btn2")  # 在col2中建立一個按紐類似st.button("按鈕2")

# 2columns, 可以用比例來設定每個collumn的寬度,將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="btn3")  # 在col1中建立一個按紐類似st.button("按鈕1")
col2.button("按鈕2", key="btn4")  # 在col2中建立一個按紐類似st.button("按鈕2")

# 3columns
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="btn5")  # 在col1中建立一個按紐類似st.button("按鈕1")
col2.button("按鈕2", key="btn6")  # 在col2中建立一個按紐類似st.button("按鈕2")
col3.button("按鈕3", key="btn7")  # 在col3中建立一個按紐類似st.button("按鈕3")
