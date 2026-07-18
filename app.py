from servicenow_client import ServiceNowClient

client = ServiceNowClient()

try:
    choice = int(input("""
    ==========================
        ServiceNow Assistant
    ==========================

    1. Create a new Incident
    2. View Incident details
    3. Update Incident
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
                "7": "Closed",
            }
            print("Incident Retreived Successfully")
            print("Incident Number   :", incident["number"])
            print("State :", state_map.get(incident["state"], incident["state"]))
            print("Short Description :", incident["short_description"])
            print("Description       :", incident["description"])

    elif choice == 3:

        incident_number = input("Incident Number:")

        incident = client.get_incident(incident_number)

        print("----------------------------------")

        if incident is None:
            print("Incident not found")
        else:
            sysid = incident["sys_id"]

            print("Incident Found!")
            print("----------------------------------")

            try:
                subchoice = int(input("""

                        1. Update Short Description
                        2. Update Description
                        3. Update Urgency
                        4. Add Work Notes
                        5. Add Customer Comments
                        6. Resolve Incident
                        7. Close Incident
                        8. Exit

                    Enter your choice: """))

                if subchoice == 1:
                    print("Current Short Description :", incident["short_description"])
                    newshort = input("New Short Description : ")
                    client.update_short_description(sysid, newshort)
                    incident = client.get_incident(incident_number)
                    print(
                        "Done!. New Short Description :", incident["short_description"]
                    )

                elif subchoice == 2:
                    print("Current Description :", incident["description"])
                    newdesc = input("New Description : ")
                    client.update_description(sysid, newdesc)

                    incident = client.get_incident(incident_number)
                    print("Done!. New Description :", incident["description"])

                elif subchoice == 3:
                    print("Current Urgency :", incident["urgency"])
                    newurg = input("New Urgency: ")
                    client.update_urgency(sysid, newurg)
                    incident = client.get_incident(incident_number)
                    print("Done!. New Urgency :", incident["urgency"])
                elif subchoice == 4:
                    work_note = input("Enter Work Notes: ")

                    client.add_work_notes(sysid, work_note)
                    print("Work Notes added successfully.")

                elif subchoice == 5:
                    customer_comment = input("Enter Customer Comment: ")
                    client.add_customer_comments(sysid, customer_comment)
                    print("Customer Comment added successfully.")

                elif subchoice == 6:

                    resolve_notes = input("Resolution Notes: ")
                    resolution_code = "Solution provided"
                    client.resolve_incident(sysid, resolution_code, resolve_notes)

                    incident = client.get_incident(incident_number)

                    print("Incident Resolved Successfully.")
                elif subchoice == 7:

                    close_notes = input("Close Notes: ")

                    payload = {
                        "state": "7",
                        "close_code": "Solved (Permanently)",
                        "close_notes": close_notes,
                    }

                    client._patch_incident(sysid, payload)

                    incident = client.get_incident(incident_number)

                    print("Incident Closed Successfully.")
                    print("State :", incident["state"])

                elif subchoice == 8:
                    exit()
                else:
                    print("Invalid choice.")
                    exit()
            except ValueError:
                print("Please enter a valid number.")
                exit()

    elif choice == 4:
        exit()

    else:
        print("Invalid choice.")
        exit()

except ValueError:
    print("Please enter a valid number.")
    exit()
