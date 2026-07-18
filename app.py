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

            resolution_codes = {
                "1": "Duplicate",
                "2": "Known error",
                "3": "No resolution provided",
                "4": "Resolved by caller",
                "5": "Resolved by change",
                "6": "Resolved by problem",
                "7": "Resolved by request",
                "8": "Solution provided",
                "9": "Workaround provided",
                "10": "User error",
            }
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
                    payload = {"short_description": newshort}

                    client.patch_incident(sysid, payload)

                    incident = client.get_incident(incident_number)
                    print(
                        "Done!. New Short Description :", incident["short_description"]
                    )

                elif subchoice == 2:
                    print("Current Description :", incident["description"])
                    newdesc = input("New Description : ")
                    payload = {"description": newdesc}

                    client.patch_incident(sysid, payload)

                    incident = client.get_incident(incident_number)
                    print("Done!. New Description :", incident["description"])

                elif subchoice == 3:
                    print("Current Urgency :", incident["urgency"])
                    newurg = input("New Urgency: ")
                    payload = {"urgency": newurg}

                    client.patch_incident(sysid, payload)

                    incident = client.get_incident(incident_number)
                    print("Done!. New Urgency :", incident["urgency"])
                elif subchoice == 4:
                    work_note = input("Enter Work Notes: ")

                    payload = {"work_notes": work_note}

                    client.patch_incident(sysid, payload)
                    print("Work Notes added successfully.")

                elif subchoice == 5:
                    customer_comment = input("Enter Customer Comment: ")

                    payload = {"comments": customer_comment}
                    client.patch_incident(sysid, payload)
                    print("Customer Comment added successfully.")

                elif subchoice == 6:

                    print("\nResolution Codes")

                    for key, value in resolution_codes.items():
                        print(f"{key}. {value}")

                    code_choice = input("\nSelect Resolution Code: ")

                    if code_choice not in resolution_codes:
                        print("Invalid Resolution Code.")
                        exit()

                    resolve_notes = input("Resolution Notes: ")

                    payload = {
                        "state": "6",
                        "close_code": resolution_codes[code_choice],
                        "close_notes": resolve_notes,
                    }

                    client.patch_incident(sysid, payload)

                    incident = client.get_incident(incident_number)

                    print("Incident Resolved Successfully.")
                elif subchoice == 7:

                    close_notes = input("Close Notes: ")

                    payload = {
                        "state": "7",
                        "close_code": "Solved (Permanently)",
                        "close_notes": close_notes,
                    }

                    client.patch_incident(sysid, payload)

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
