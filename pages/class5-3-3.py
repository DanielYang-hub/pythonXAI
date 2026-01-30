import streamlit as st
from openai import OpenAI

# 建立 client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 初始化對話紀錄
if "history" not in st.session_state:
    st.session_state.history = []

# 系統訊息初始化
if "system_message" not in st.session_state:
    st.session_state.system_message = "please use English to chat"

# 模型初始化
if "model" not in st.session_state:
    st.session_state.model = "gpt-5-mini"

# 頁面設定
st.title("🪄 我的 AI 聊天機器人")

# 調整系統訊息和模型
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )
with col2:
    st.session_state.model = st.selectbox(
        "選擇模型", ["gpt-5-mini", "gpt-4o-mini", "gpt-4o"]
    )
with col3:
    if st.button("🗑️"):
        st.session_state.history = []
        st.rerun()

# 顯示歷史對話
for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="✨").write(message["content"])

# 聊天輸入框
user_input = st.chat_input("請輸入訊息")
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})

    messages = [{"role": "system", "content": st.session_state.system_message}]
    messages += st.session_state.history

    response = client.chat.completions.create(
        model=st.session_state.model,
        messages=messages,
    )

    assistant_message = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": assistant_message})

    st.rerun()
