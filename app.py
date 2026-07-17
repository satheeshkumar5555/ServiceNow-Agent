from servicenow_client import ServiceNowClient

client = ServiceNowClient()

try:
    choice = int(input("""
    ==========================
        ServiceNow Assistant
    ==========================

    1. Create a new Incident
    2. View Incident details
    3. Update Incident Fields (Short Description, Description, Urgency)
    4. Exit

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

                incident_number = input("Incident Number:")

                incident = client.get_incident(incident_number)
            

                print("----------------------------------")

                if incident is None:
                    print("Incident not found")
                else:
                    sysid = incident["sys_id"]
                    state_map = {
                    "1": "New",
                    "2": "In Progress",
                    "3": "On Hold",
                    "6": "Resolved",
                    "7": "Closed"
                }
                    print("Incident Found!")
                print("----------------------------------")
                try:
                    subchoice = int(input("""

                    1. Update Short Description
                    2. Update Description
                    3. Update Urgency
                    4. Exit

                Enter your choice: """))

                    if subchoice == 1:
                        print("Current Short Description :", incident["short_description"])
                        newshort = input("New Short Description : ")
                        payload = {
                            "short_description": newshort
                        }
                        
                        
                        client.patch_incident(sysid, payload)
                        
                        incident = client.get_incident(incident_number)
                        print("Done!. New Short Description :", incident["short_description"])

                    if subchoice == 2:
                            print("Current Description :", incident["description"])
                            newdesc = input("New Description : ")
                            payload = {
                            "description": newdesc
                        }
                            
                            client.patch_incident(sysid, payload)
                            
                            incident = client.get_incident(incident_number)
                            print("Done!. New Description :", incident["description"])

                    if subchoice == 3:
                            print("Current Urgency :", incident["urgency"])
                            newurg = input("New Urgency: ")
                            payload = {
                            "urgency": newurg
                        }
                            
                            
                            client.patch_incident(sysid, payload)
                            
                            incident = client.get_incident(incident_number)
                            print("Done!. New Urgency :", incident["urgency"])
                    if subchoice == 4:
                        exit()
                    else:
                        print("Invalid choice.")
                        exit()
                except ValueError:
                    print("Please enter a valid number.")
                    exit()    

    if choice == 4:
        exit()

    else:
        print("Invalid choice.")
        exit()

except ValueError:
    print("Please enter a valid number.")
    exit()       