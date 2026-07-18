from agent import ServiceNowAgent

agent = ServiceNowAgent()

print("ServiceNow AI Assistant")
print("Type 'exit' to quit.\n")

while True:

    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    response = agent.chat(user_message)

    print(f"\nAssistant: {response}\n")
