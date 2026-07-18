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
                        "You are a ServiceNow assistant. "
                        "Whenever the user's request can be completed using one of the available tools, "
                        "you MUST use the appropriate tool instead of asking follow-up questions. "
                        "If required parameters can be reasonably inferred from the user's request, infer them."
                    )
                }
            ],
        }

        if tools:
            request["toolConfig"] = {"tools": tools}

        return self.client.converse(**request)
