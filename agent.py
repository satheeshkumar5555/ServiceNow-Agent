from llm_client import LLMClient
from servicenow_client import ServiceNowClient


class ServiceNowAgent:

    def __init__(self):
        self.llm = LLMClient()
        self.servicenow = ServiceNowClient()

    def chat(self, user_message):
        return self.llm.ask(user_message)
