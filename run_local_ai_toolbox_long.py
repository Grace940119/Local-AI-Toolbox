import os
import shutil
import tempfile
from llama_cpp import Llama

# ===== 模型路徑 =====(使用時注意更改路徑)
ORIGINAL_MODEL_PATH = r"C:\Grace\大學\大三\大三上\軟體工程\期中\ai-toolbox-local\models\mistral-7b-instruct.gguf"

# ===== 複製模型到臨時資料夾（避免中文路徑問題） =====
TEMP_DIR = tempfile.gettempdir()
MODEL_FILENAME = os.path.basename(ORIGINAL_MODEL_PATH)
TEMP_MODEL_PATH = os.path.join(TEMP_DIR, MODEL_FILENAME)

if not os.path.exists(ORIGINAL_MODEL_PATH):
    raise ValueError(f"模型不存在，請確認路徑：{ORIGINAL_MODEL_PATH}")

if not os.path.exists(TEMP_MODEL_PATH):
    shutil.copyfile(ORIGINAL_MODEL_PATH, TEMP_MODEL_PATH)

# ===== 建立 Llama 實例 =====
llm = Llama(
    model_path=TEMP_MODEL_PATH,
    n_ctx=8192,      # 增加上下文最大 token
    n_threads=4,
    verbose=False
)

# ===== 歷史對話（滾動上下文） =====
history = []
MAX_HISTORY = 10  # 最多保留最近 10 輪對話，避免超出 n_ctx

# ===== 互動函式 =====
def chat(prompt):
    global history
    # 構建 prompt，保留最近幾輪對話
    context = history[-MAX_HISTORY:]
    full_prompt = ""
    for q, a in context:
        full_prompt += f"問：{q}\n答：{a}\n"
    full_prompt += f"問：{prompt}\n答："

    # 自動加上中文提示
    full_prompt = f"用中文回答：{full_prompt}"

    try:
        resp = llm(prompt=full_prompt, max_tokens=3000)  # 設大值，生成長回答
        if "choices" in resp and resp["choices"]:
            answer = resp["choices"][0]["text"].strip()
            print("\nAI 回應：")
            print(answer)
            # 儲存到歷史
            history.append((prompt, answer))
        else:
            print("[模型沒有生成回應]")
    except Exception as e:
        print(f"[生成錯誤] {e}")

# ===== 主程式 =====
if __name__ == "__main__":
    print("=== 本地 AI 百寶箱（中文模式 + 長對話 + 無字數限制） ===")
    print("功能示範：小詩、問答、計算、翻譯…可生成很長內容")
    while True:
        user_input = input("\n輸入你的問題 (輸入 exit 離開)：")
        if user_input.lower() in ["exit", "quit"]:
            print("再見！")
            break
        chat(user_input)
