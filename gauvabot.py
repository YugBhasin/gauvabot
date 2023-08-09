import openai

openai.api_key = "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"

messages = []
system_msg = input("What is your name?\n")
messages.append({"role": "system", "content": system_msg})

print("Hey there!,glad to meet you",system_msg)
print("How may I assist you?")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")