import openai

openai.api_key = "dusri api key dalni hai"

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


https://code-with-me.global.jetbrains.com/2KUMNsoX3BBSnXDPxc8z8A#p=PC&fp=4673EF97DACBC940CDACEF4A8EEAA46222BB1280235FD0D93FCA983CE34111A2&newUi=true
