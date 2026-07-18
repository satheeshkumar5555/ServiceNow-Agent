CREATE_INCIDENT_TOOL = {
    "toolSpec": {
        "name": "create_incident",
        "description": "Create a new ServiceNow incident.",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "short_description": {
                        "type": "string",
                        "description": "A short summary of the issue.",
                    },
                    "description": {
                        "type": "string",
                        "description": "A detailed description of the issue.",
                    },
                },
                "required": ["short_description", "description"],
            }
        },
    }
}
