CREATE_INCIDENT_TOOL = {
    "toolSpec": {
        "name": "create_incident",
        "description": (
            "Use this tool to create a ServiceNow incident whenever a user reports "
            "an IT problem such as a hardware issue, software issue, login problem, "
            "network problem, email issue, VPN issue, or requests assistance from the "
            "IT help desk. If enough information is available, infer the short "
            "description and description and create the incident without asking "
            "unnecessary follow-up questions."
        ),
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "short_description": {
                        "type": "string",
                        "description": (
                            "Generate a concise one-line summary suitable for the "
                            "ServiceNow Short Description field."
                        ),
                    },
                    "description": {
                        "type": "string",
                        "description": (
                            "Generate a detailed description suitable for the "
                            "ServiceNow Description field based on the user's problem."
                        ),
                    },
                },
                "required": ["short_description", "description"],
            }
        },
    }
}
