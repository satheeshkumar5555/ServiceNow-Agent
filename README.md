# ServiceNow AI Agent with Amazon Bedrock

## Overview

This project demonstrates how to build an AI-powered ServiceNow assistant using Python and Amazon Bedrock.

The application combines a reusable ServiceNow REST API client with Amazon Bedrock's native Tool Use capability, allowing users to interact with ServiceNow using natural language.

Instead of manually parsing user prompts, the Large Language Model (LLM) decides which ServiceNow operation to execute and automatically extracts the required parameters before invoking the appropriate tool.

---

## Features

### ServiceNow SDK

- Create Incident
- Get Incident
- Update Short Description
- Update Description
- Update Urgency
- Add Work Notes
- Add Customer Comments
- Resolve Incident
- Close Incident

### AI Agent

- Natural language interaction
- Amazon Bedrock (Nova) integration
- Native Bedrock Tool Use
- Automatic tool selection
- Automatic parameter extraction
- AI-driven ServiceNow incident creation

---

## Architecture

```text
                    +------------------+
                    |      User        |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |   agent_app.py   |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | ServiceNowAgent  |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |   LLMClient      |
                    | Amazon Bedrock   |
                    +--------+---------+
                             |
                             v
                    Native Tool Use
                             |
                             v
                    +------------------+
                    | ServiceNowClient |
                    +--------+---------+
                             |
                             v
                    ServiceNow REST API
```

---

## Project Structure

```text
ServiceNow-Agent/
│
├── app.py                  # Manual ServiceNow CLI
├── agent_app.py            # AI chat interface
├── agent.py                # AI agent orchestration
├── llm_client.py           # Amazon Bedrock client
├── bedrock_tools.py        # Bedrock tool definitions
├── servicenow_client.py    # ServiceNow REST SDK
├── config.py               # Configuration
├── requirements.txt
├── README.md
├── .env                    # Environment variables (not committed)
└── .gitignore
```

---

## Technologies Used

- Python
- Amazon Bedrock
- Amazon Nova
- Boto3
- ServiceNow REST API
- python-dotenv

---

## How It Works

1. User enters a request in natural language.

Example:

```
Create an incident because Outlook crashes every morning.
```

2. The AI agent sends the request to Amazon Bedrock.

3. Bedrock determines that the request requires the `create_incident` tool.

4. Bedrock extracts the required parameters.

Example:

```json
{
  "short_description": "Outlook crashes every morning",
  "description": "Outlook is crashing every morning, causing disruption to work processes."
}
```

5. The agent executes the corresponding ServiceNow REST API.

6. The incident is created successfully in ServiceNow.

---

## Example

**User**

```
Create an incident because Outlook crashes every morning.
```

**Agent**

- Detects that an incident needs to be created.
- Selects the `create_incident` tool.
- Extracts the incident details.
- Calls the ServiceNow REST API.
- Creates the incident automatically.

---

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd ServiceNow-Agent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file.

```text
INSTANCE=https://your-instance.service-now.com
USERNAME=your_username
PASSWORD=your_password

AWS_REGION=eu-central-1
BEDROCK_MODEL_ID=eu.amazon.nova-2-lite-v1:0
```

---

## Running the Application

### Manual ServiceNow CLI

```bash
python app.py
```

### AI Agent

```bash
python agent_app.py
```

Example:

```
You:
Create an incident because Outlook crashes every morning.
```

---

## Current Capabilities

### ServiceNow Operations

- ✅ Create Incident
- ✅ Get Incident
- ✅ Update Short Description
- ✅ Update Description
- ✅ Update Urgency
- ✅ Add Work Notes
- ✅ Add Customer Comments
- ✅ Resolve Incident
- ✅ Close Incident

### AI Capabilities

- ✅ Natural language understanding
- ✅ Native Bedrock Tool Use
- ✅ Automatic tool selection
- ✅ Automatic parameter extraction
- ✅ ServiceNow integration

---

## Learning Outcomes

This project demonstrates practical experience with:

- REST API integration
- Object-Oriented Programming (OOP)
- Python SDK development
- Amazon Bedrock Converse API
- Amazon Bedrock Native Tool Use
- AI Agent architecture
- Enterprise application integration
- ServiceNow automation

---

## Future Enhancements

- Support multiple ServiceNow tools
- Multi-turn conversations
- Conversation memory
- Logging and monitoring
- Retrieval-Augmented Generation (RAG)
- Authentication improvements
- Multiple enterprise integrations
- Web interface using Streamlit or Flask

---

## Screenshots

Add screenshots here demonstrating:

- AI conversation
- Tool invocation
- ServiceNow incident creation

---

## Author

Satheesh Kumar

Cloud Security Engineer | Python | AWS | Amazon Bedrock | ServiceNow | AI Agents