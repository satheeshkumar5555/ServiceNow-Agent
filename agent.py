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

    def chat(self, user_message, messages):

        messages.append({"role": "user", "content": [{"text": user_message}]})
        response = self.llm.converse(messages=messages, tools=[CREATE_INCIDENT_TOOL])

        assistant_message = response["output"]["message"]

        messages.append(assistant_message)

        tool = None

        for block in assistant_message["content"]:
            if "toolUse" in block:
                tool = block["toolUse"]
                break

        # No tool requested - just return the assistant's text
        if tool is None:
            return assistant_message["content"][0]["text"]

        # Tool requested
        result = self.execute_tool(tool["name"], tool["input"])

        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "toolResult": {
                            "toolUseId": tool["toolUseId"],
                            "content": [{"json": result}],
                        }
                    }
                ],
            }
        )

        final_response = self.llm.converse(
            messages=messages, tools=[CREATE_INCIDENT_TOOL]
        )

        messages.append(final_response["output"]["message"])

        return final_response["output"]["message"]["content"][0]["text"]
