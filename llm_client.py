import boto3

from config import AWS_REGION, BEDROCK_MODEL_ID


class LLMClient:

    def __init__(self):
        self.client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

        self.model_id = BEDROCK_MODEL_ID

    def ask(self, prompt):

        response = self.client.converse(
            modelId=self.model_id,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
        )

        return response["output"]["message"]["content"][0]["text"]

    def converse(self, messages, tools=None):

        request = {
            "modelId": self.model_id,
            "messages": messages,
            "system": [
                {
                    "text": (
                        "You are an AI-powered ServiceNow IT Support Assistant.\n\n"
                        "Your responsibilities are:\n"
                        "- Help users report IT issues.\n"
                        "- Use the available ServiceNow tools whenever appropriate.\n"
                        "- Answer questions about incidents using the available tools.\n\n"
                        "When a user reports an IT issue such as hardware problems, software problems, "
                        "login issues, VPN problems, email issues, or network problems, "
                        "use the appropriate tool without asking unnecessary follow-up questions if enough "
                        "information can reasonably be inferred.\n\n"
                        "Maintain a calm, professional, and empathetic tone.\n"
                        "If the user reports a problem, first acknowledge the inconvenience.\n"
                        "Avoid celebratory phrases such as 'Great!', 'Awesome!', or 'Fantastic!'.\n\n"
                        "After completing an action, clearly explain:\n"
                        "- What was done.\n"
                        "- Any important details returned by the tool.\n"
                        "- What the user should expect next.\n"
                        "- Never claim that you have performed an action unless you have actually used a tool to perform it.\n"
                        "- If the required tool is unavailable, clearly tell the user that you cannot perform that action..\n"
                        "- Do not imply that an incident has been updated, modified, escalated, assigned, or resolved unless the corresponding tool has been successfully executed.\n\n"
                    )
                }
            ],
        }

        if tools:
            request["toolConfig"] = {"tools": tools}

        return self.client.converse(**request)
