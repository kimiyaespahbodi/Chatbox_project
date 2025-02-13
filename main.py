import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
