from llm_client import LLMClient
from servicenow_client import ServiceNowClient
from bedrock_tools import CREATE_INCIDENT_TOOL


class ServiceNowAgent:

    def __init__(self):
        self.llm = LLMClient()
        self.servicenow = ServiceNowClient()

    def execute_tool(self, tool_name, tool_input):

        if tool_name == "create_incident":
            return self.servicenow.create_incident(
                tool_input["short_description"], tool_input["description"]
            )

        raise ValueError(f"Unknown tool: {tool_name}")

    from bedrock_tools import CREATE_INCIDENT_TOOL

    def chat(self, user_message):

        messages = [{"role": "user", "content": [{"text": user_message}]}]

        response = self.llm.converse(messages=messages, tools=[CREATE_INCIDENT_TOOL])

        if response["stopReason"] == "tool_use":

            tool = response["output"]["message"]["content"][0]["toolUse"]

            result = self.execute_tool(tool["name"], tool["input"])

            print(f"Incident created: {result['number']}")

            return "Tool executed successfully."

        return response["output"]["message"]["content"][0]["text"]
