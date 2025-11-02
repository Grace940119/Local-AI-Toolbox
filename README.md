# 用Python+ChatGPT製作一個AI實用百寶箱
## 1️⃣問題：我想用 Python + ChatGPT 製作一個 AI 實用百寶箱
- 建議使用 Python + Gradio 建立 Web 介面
- 功能可包含：聊天、摘要、翻譯、程式碼解釋
- 提供初步範例程式碼框架
- 可在 Colab 執行，方便測試
<img width="479" height="382" alt="image" src="https://github.com/user-attachments/assets/eb0d411f-640d-4091-a8cb-24f3cefd8355" />
<img width="479" height="392" alt="image" src="https://github.com/user-attachments/assets/bcdc71db-cb14-444a-804e-87046a299493" />

---
### 因為曾經上課學過 Google Colab ，所以想從 Google Colab 來上手。

<img width="473" height="395" alt="image" src="https://github.com/user-attachments/assets/0d035060-55f7-4e15-9008-57a2abd66736" />
<img width="475" height="396" alt="image" src="https://github.com/user-attachments/assets/6f4595d1-9369-49b7-9675-dfbf602fa179" />

---
<img width="467" height="392" alt="image" src="https://github.com/user-attachments/assets/6293e112-8cd2-4aab-abbf-28b0fc35f4cb" />
<img width="467" height="394" alt="image" src="https://github.com/user-attachments/assets/36de7704-ebf1-4fd4-bd5b-0f4b66d48d91" />

---
<img width="463" height="387" alt="image" src="https://github.com/user-attachments/assets/49875efc-4d24-40bd-9456-d2eec02fa7e7" />
<img width="467" height="394" alt="image" src="https://github.com/user-attachments/assets/c2e62f0f-7172-48a4-a2e4-39428ce20403" />

---
<img width="468" height="381" alt="image" src="https://github.com/user-attachments/assets/bb9b1276-fa6f-424a-a1e2-8c0108e59e3e" />

---
## 2️⃣問題：ChatGPT 回覆一直錯誤，是否一定要金鑰？
- 對 OpenAI API 必須有可用額度或金鑰，否則會出現錯誤
- 429 錯誤表示「額度不足」
- 提供方案：
  1. 升級方案或付費增加額度
  2. 等免費額度重置
  3. 改用免費模型（Hugging Face DialoGPT-small 等）
 
<img width="494" height="376" alt="image" src="https://github.com/user-attachments/assets/76d13c44-a71b-4ff9-ab2d-d2f573c74d59" />
<img width="478" height="395" alt="image" src="https://github.com/user-attachments/assets/031ab3fe-c0e8-4f8d-bc0e-5c7a959cc62c" />

---
<img width="479" height="359" alt="image" src="https://github.com/user-attachments/assets/e56109eb-6c7d-471e-bc57-761438a14b2e" />

---

## 3️⃣問題：翻譯結果不正確，刪除摘要和程式碼解釋
- DialoGPT 不是專門翻譯模型
- 改用 Hugging Face 專用翻譯模型：
  - 中文→英文：`Helsinki-NLP/opus-mt-zh-en`
  - 英文→中文：`Helsinki-NLP/opus-mt-en-zh`
- 簡化成 **只保留聊天 + 雙向翻譯功能**
- 完全免費、免金鑰、直接使用 Gradio 介面

<img width="478" height="380" alt="image" src="https://github.com/user-attachments/assets/fde27892-cd35-4aa4-ac81-01f13f30bb33" />
<img width="474" height="380" alt="image" src="https://github.com/user-attachments/assets/70b3ecbd-6b53-4901-a859-e0d624b42f70" />

---
<img width="470" height="354" alt="image" src="https://github.com/user-attachments/assets/89acd466-b48f-487f-ba29-6bfa980c6d5e" />

---

## 成果如下：
### Google Colab
<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/c9750f0a-bccf-4bac-93bc-b0013ffe6d50" />
<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/b4416435-f8e2-4836-9510-e8766ba91a0e" />

### Gradio
<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/8ea70910-9bd8-4d05-a573-378bcf67295b" />
<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/ea0237a8-f41c-4469-9b85-2779dc9bd108" />

https://colab.research.google.com/drive/1fIqzvuJNaF7-3LPP-ll7mGi8op43C852?usp=sharing

### 但我們不甘於只有聊天+翻譯，Gradio網站這個聊天機器甚至有點笨拙，所以後來打算用Visual Studio Code重做一遍，學習使用新環境開發程式。
## 1️⃣問題：在Vitual Studio Code用Python+ChatGPT製作一個AI實用百寶箱
- 功能可包含：互動聊天、文字摘要、程式碼說明、圖像生成
- 提供初步範例程式碼框架

<img width="479" height="324" alt="image" src="https://github.com/user-attachments/assets/a196125c-077d-4ed7-9b95-19220da0e8f9" />
<img width="473" height="334" alt="image" src="https://github.com/user-attachments/assets/c285eb9f-80e1-4a77-afd9-7910395531d1" />

---
<img width="476" height="317" alt="image" src="https://github.com/user-attachments/assets/4f18ec1d-731b-4e76-a8a3-6222982ea148" />
<img width="472" height="307" alt="image" src="https://github.com/user-attachments/assets/5346e990-dfe9-4ddf-99ae-17366e5ee9c2" />

---
<img width="467" height="328" alt="image" src="https://github.com/user-attachments/assets/1b2cdae0-1957-4b57-b4b6-cb1ea140e854" />
<img width="478" height="332" alt="image" src="https://github.com/user-attachments/assets/0d34de86-8d03-4eb2-9118-3acf191d2959" />

---
<img width="469" height="286" alt="image" src="https://github.com/user-attachments/assets/ba64d280-231b-45d6-b262-62d2b52b3605" />
<img width="470" height="244" alt="image" src="https://github.com/user-attachments/assets/aef7875b-3eab-4317-b3ca-3d31e777cc12" />

---
<img width="475" height="329" alt="image" src="https://github.com/user-attachments/assets/30fad7ef-66b1-4083-a54f-fdb00951b85d" />
<img width="471" height="318" alt="image" src="https://github.com/user-attachments/assets/76ce8037-0854-481d-9056-d86098e15a33" />

---
<img width="466" height="331" alt="image" src="https://github.com/user-attachments/assets/7e687c39-bd7c-4e91-995d-31e42ca7b810" />
<img width="482" height="325" alt="image" src="https://github.com/user-attachments/assets/dd90996e-97c6-4bdd-9dfb-0860e1e2927b" />

---
<img width="472" height="326" alt="image" src="https://github.com/user-attachments/assets/64f7a6d6-b3aa-4297-8b52-dd09be1ac343" />

---

## 2️⃣問題：明明有建立檔案，錯誤提示一直顯示查無檔案。
#### Visual Studio Code (VS Code)
- 功能：主要是 程式編輯器，可以寫 Python 檔案、Markdown、甚至跑 Terminal。
- 限制：VS Code 本身沒有 Python 環境，它只是一個工具，用來編輯與呼叫你系統中安裝的 Python。
- 因此：當你在 VS Code 的 Terminal 嘗試執行 conda activate opencv 或 python，如果路徑、環境沒設好，就會出現找不到 conda 或 Python 的問題。
#### PowerShell
- 功能：Windows 預設的 命令列介面 (CLI)。
- 原因：
  - 用來執行 Conda 指令 (conda activate …)。
  - 用來建立資料夾、檢查路徑。
  - 可以直接啟動 Python 互動模式 (python)。
- 問題：
  - PowerShell 預設執行政策會阻擋腳本執行 (ExecutionPolicy) → 需要用 Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 解除限制。
  - 語法和 Python 不同，不能直接寫 from llama_cpp import Llama 或 resp = llm.create(...)，那是 Python 語法，要在 Python 互動模式下執行。
#### Anaconda Prompt
- 功能：專門為 Conda 環境管理 設計的 CLI。
- 用途：
  - 建立與管理 Python 環境。
  - 安裝套件（pip install / conda install）。
  - 確保你的 Python 版本與模型套件相容。
- 為什麼有時直接用 PowerShell 也可以：
  - 因為 Conda 可以初始化 PowerShell，讓你在 PowerShell 也能用 conda activate。
  - 但是初次設定前，PowerShell 可能找不到 conda。
#### Python 互動模式 (python 或 .py 檔案)
- 功能：執行 Python 語法、呼叫模型。
- 原因：
  - 程式是 Python (utils_local.py, run_local_ai.py)。
  - PowerShell / Anaconda Prompt 只是 載入 Python 的通道。
- 注意：
  - Python 語法要在 >>> 互動模式或 .py 檔案執行，不能直接在 PowerShell 寫 from llama_cpp import Llama，否則報錯。
### 我們用 PowerShell 和 Anaconda Prompt 檢查出來，最後發現是 GPT 給的路徑錯誤

<img width="482" height="332" alt="image" src="https://github.com/user-attachments/assets/09e13e2d-facb-4982-8a7d-1a9379e55e9f" />
<img width="482" height="331" alt="image" src="https://github.com/user-attachments/assets/f047a72e-f189-4035-91ac-09589b86e92d" />

---
<img width="473" height="265" alt="image" src="https://github.com/user-attachments/assets/0238a947-6354-49e6-8825-09fdbaf22562" />

---

## 3️⃣問題：回答是中文，且希望是沒有字數限制
- 中文模式：自動加上「用中文回答」。
- 長對話：最多保留最近 10 輪問題與回答，AI 可以上下文連貫回應。
- 無字數限制：max_tokens 設成 3000，n_ctx 8192，能生成長篇回答。
- 滾動上下文：超過 MAX_HISTORY，舊對話自動捨棄，避免超出模型限制。
- 多功能：小詩、問答、計算、翻譯等都可以直接輸入中文。

<img width="474" height="200" alt="image" src="https://github.com/user-attachments/assets/01c1c779-71bb-4cbc-8de9-20ecde3a2055" />
<img width="497" height="271" alt="image" src="https://github.com/user-attachments/assets/362514b2-8f2d-4b5b-9d52-a0411e54d67c" />

---
<img width="473" height="230" alt="image" src="https://github.com/user-attachments/assets/e9b237b4-0ab6-4244-9f4c-11fdc2088914" />
<img width="483" height="326" alt="image" src="https://github.com/user-attachments/assets/40396dbf-20b4-4166-bcdf-ae7ec47b08b6" />

---
<img width="473" height="308" alt="image" src="https://github.com/user-attachments/assets/501b8f02-16d9-4208-8c6e-0ba2b9eb6557" />
<img width="472" height="331" alt="image" src="https://github.com/user-attachments/assets/f4447b80-1793-4aed-90f1-b67d1cd62084" />

---
<img width="473" height="332" alt="image" src="https://github.com/user-attachments/assets/c6286e69-5e91-4f0e-8712-140271ba8d02" />

---

## 成果如下：
### PowerShell
<img width="761" height="464" alt="image" src="https://github.com/user-attachments/assets/57efca1b-e803-4c25-b0c4-66695573b6dc" />

### Visual Studio Code (程式部分)
<img width="476" height="427" alt="image" src="https://github.com/user-attachments/assets/94a8f0a4-f3aa-4eb9-908b-bb02e4b0e424" />
<img width="618" height="491" alt="image" src="https://github.com/user-attachments/assets/cede5473-7ae2-4c66-8d39-a846dae8dddc" />
<img width="518" height="457" alt="image" src="https://github.com/user-attachments/assets/00978f1c-0008-44a0-9e2d-6345a1df7e4c" />

### 專案結構
    ai-toolbox-local/
    ├─ __pycache__/
    |    └─utils_local.cpython-39.pyc
    ├─ models/
    |    └─ mistral-7b-instruct.gguf
    ├─ utils_local.py
    └─ run_local_ai_toolbox_long.py

#### (量化模型檔案太大不能上傳)

## 結語

從 Google Colab 到 VS Code、PowerShell、再到 Anaconda Prompt，經過這一路的摸索。

Colab 讓我們先體驗怎麼跑模型，很方便但聊天機器不太聰明； VS Code 是我們最終寫程式的地方，PowerShell 用來下指令，Anaconda 則管環境，做出執行速度較慢，但比較聰明且功能較多的 AI 百寶箱。

雖然中間遇到很多錯誤，但每解決一個問題，就多學到一點。最後看著自己的「AI 百寶箱」真的能跑起來，我們覺得超有成就感。
