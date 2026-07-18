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
