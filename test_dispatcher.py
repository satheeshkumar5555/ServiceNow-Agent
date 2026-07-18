from agent import ServiceNowAgent

agent = ServiceNowAgent()

result = agent.execute_tool(
    "create_incident",
    {"short_description": "Dispatcher Test", "description": "Testing execute_tool()"},
)

print(result)
