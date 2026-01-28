import streamlit as st

st.title("數字金字塔")
a = st.number_input("高度", min_value=1, step=1)
for i in range(1, int(a) + 1):
    line = ""
    for j in range(i):
        line += str(i)
    st.write(line)


import streamlit as st

st.title("箭頭金字塔")
n = st.number_input("請輸入箭頭層數", min_value=1, step=1)

a = ""
for i in range(1, n + 1):
    a = a + (" " * (n - i) + "*" * (i * 2 - 1) + "\n")
for i in range(n):
    a = a + (" " * (n - 1) + "*" + "\n")
st.markdown(f"```\n箭頭金字塔:\n{a}```")
