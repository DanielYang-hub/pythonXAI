import openai  # pip install openai
from dotenv import load_dotenv
import os

load_dotenv()  # 載入 .env 檔案內容

# 設定 API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化對話歷史
message = [{"role": "system", "content": "請使用繁體中文進行後續對話"}]

while True:
    user_input = input("你: ")  # 終端機輸入使用者訊息
    if user_input.lower() in ["exit", "quit"]:
        break

    message.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-5-mini",  # 請確認你的可用模型
        messages=message,  # 注意這裡必須是 messages
    )

    assistant_message = response.choices[0].message.content
    print(f"AI: {assistant_message}")

    message.append({"role": "assistant", "content": assistant_message})
