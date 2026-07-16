from servicenow_client import ServiceNowClient

client = ServiceNowClient()

choice = int(input("""
==========================
    ServiceNow Assistant
==========================

1. Create a new Incident
2. View Incident details
3. Exit

Enter your choice: """))

if choice == 1:
    
    short = input("Short Description : ")

    desc = input("Description       : ")

    incident = client.create_incident(short, desc)

    print()

    print("Incident Created Successfully")

    print("----------------------------------")

    print("Incident :", incident["number"])


elif choice == 2:


    incident_number = input("Incident Number:")

    incident = client.get_incident(incident_number)

   
    print("----------------------------------")

    if incident is None:
        print("Incident not found")
    else:

        state_map = {
        "1": "New",
        "2": "In Progress",
        "3": "On Hold",
        "6": "Resolved",
        "7": "Closed"
    }
        print("Incident Retreived Successfully")
        print("Incident Number   :", incident["number"])
        print("State :", state_map.get(incident["state"], incident["state"]))
        print("Short Description :", incident["short_description"])
        print("Description       :", incident["description"])
   
if choice == 3:
    exit

    