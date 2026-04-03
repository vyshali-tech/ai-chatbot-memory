# 🧠 AI Conversational Chatbot with Persistent Memory

## 📌 Project Overview
## 📸 Demo Screenshot

![Chatbot Screenshot](screenshot.png)

This project is an AI-powered chatbot built using Python and a local AI model through Ollama.

Unlike basic chatbots, this system remembers past conversations by saving chat history into a file. Even after restarting the program, the chatbot can recall previous messages.

---

## 🚀 Features

- 🤖 Local AI chatbot using Ollama
- 🧠 Persistent conversation memory
- 📜 Show chat history command
- 🧹 Reset memory command
- ⚡ Memory size control
- 🧩 Modular Python structure

---

## 🛠 Technologies Used

- Python
- Ollama
- phi3:mini model
- JSON (memory storage)

---

## 📂 Project Structure

```
ai_chatbot_memory/
│
├── chatbot.py
├── llm_api.py
├── memory.py
├── memory.json
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ▶️ How to Run the Project

### Step 1 — Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 2 — Install Ollama

Download from:

https://ollama.com

---

### Step 3 — Download Model

```
ollama run phi3:mini
```

---

### Step 4 — Run Chatbot

```
python chatbot.py
```
---
## 💬 Available Commands

- `exit` → Close chatbot  
- `reset memory` → Clear saved memory  
- `show history` → Display previous messages  

---
---

## ⚙️ How It Works

1. The chatbot takes user input.
2. The input is stored in a memory file (`memory.json`).
3. Previous messages are loaded to maintain conversation context.
4. The messages are sent to the local AI model using Ollama.
5. The AI generates a response.
6. The response is saved back into memory.
7. Users can reset memory or view history using commands.

This allows the chatbot to remember conversations even after restarting.
## 🎯 Future Improvements

- Add web interface  
- Add API-based models  
- Improve memory intelligence  
- Add user profiles  

---

## 👩‍💻 Author

Vyshali