import os
from llama_cpp import Llama

# 模型路徑(使用時注意更改路徑)
MODEL_PATH = r"C:\Grace\大學\大三\大三上\軟體工程\期中\ai-toolbox-local\models\mistral-7b-instruct.gguf"

# 檢查模型是否存在
if not os.path.exists(MODEL_PATH):
    raise ValueError(f"模型不存在，請確認路徑：{MODEL_PATH}")

# 建立 Llama 實例
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=4,
    verbose=False
)

# 互動函式
def chat(prompt):
    try:
        # 新版 llama_cpp 使用 __call__ 或 llm(prompt=...)
        resp = llm(prompt=prompt, max_tokens=150)
        if "choices" in resp and resp["choices"]:
            print("\nAI 回應：")
            print(resp["choices"][0]["text"])
        else:
            print("[模型沒有生成回應]")
    except Exception as e:
        print(f"[生成錯誤] {e}")

# 主程式
if __name__ == "__main__":
    print("=== 本地 AI 百寶箱 ===")
    while True:
        user_input = input("\n輸入你的問題 (輸入 exit 離開)：")
        if user_input.lower() in ["exit", "quit"]:
            print("再見！")
            break
        chat(user_input)
