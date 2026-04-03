import ollama

def get_llm_response(messages):

    response = ollama.chat(
        model="phi3:mini",
        messages=messages
    )

    return response["message"]["content"]