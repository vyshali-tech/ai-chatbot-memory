from llm_api import get_llm_response
from memory import load_memory, save_memory

print("🤖 AI Chatbot with Memory Started!")
print("Type 'exit' to quit.")
print("Type 'reset memory' to clear memory.")
print("Type 'show history' to view past chats.\n")

# Load previous memory
messages = load_memory()

# Add system prompt if empty
if len(messages) == 0:
    messages.append({
        "role": "system",
        "content": "You are a helpful AI assistant. Give short, clear answers."
    })

while True:

    user_input = input("You: ")

    # ✅ Exit FIRST
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    # ✅ Reset memory
    if user_input.lower() == "reset memory":
        messages = []
        messages.append({
            "role": "system",
            "content": "You are a helpful AI assistant. Give short, clear answers."
        })
        save_memory(messages)
        print("🧹 Memory cleared successfully.")
        continue

    # ✅ Show history command
    if user_input.lower() == "show history":

        print("\n📜 Chat History:\n")

        for msg in messages:
            if msg["role"] == "user":
                print("You:", msg["content"])
            elif msg["role"] == "assistant":
                print("Bot:", msg["content"])

        print("\n--- End of History ---\n")

        continue

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Get AI response
    response = get_llm_response(messages)

    print("Bot:", response)

    # Save assistant response
    messages.append({
        "role": "assistant",
        "content": response
    })

    save_memory(messages)