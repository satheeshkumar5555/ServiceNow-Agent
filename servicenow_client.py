import requests
from config import INSTANCE, USERNAME, PASSWORD


class ServiceNowClient:

    def create_incident(self, short_description, description):

        url = f"{INSTANCE}/api/now/table/incident"

        payload = {"short_description": short_description, "description": description}

        response = requests.post(
            url,
            auth=(USERNAME, PASSWORD),
            json=payload,
            headers={"Accept": "application/json", "Content-Type": "application/json"},
        )

        if response.status_code == 201:

            return response.json()["result"]

        raise Exception(response.text)

    def get_incident(self, incident_number):

        url = f"{INSTANCE}/api/now/table/incident"
        params = {
            "sysparm_query": f"number={incident_number}",
            "sysparm_fields": "sys_id,number,short_description,description,state,urgency",
        }

        response = requests.get(
            url,
            auth=(USERNAME, PASSWORD),
            params=params,
            headers={"Accept": "application/json", "Content-Type": "application/json"},
        )

        if response.status_code == 200:
            result = response.json()["result"]

        if len(result) == 0:
            return None
        else:
            return result[0]

        raise Exception(response.text)

    def _patch_incident(self, sysid, payload):

        url = f"{INSTANCE}/api/now/table/incident/{sysid}"

        response = requests.patch(
            url,
            auth=(USERNAME, PASSWORD),
            json=payload,
            headers={"Accept": "application/json", "Content-Type": "application/json"},
        )

        if response.status_code == 200:

            return response.json()["result"]

        raise Exception(response.text)

    def update_short_description(self, sysid, short_description):

        payload = {"short_description": short_description}

        return self._patch_incident(sysid, payload)

    def update_description(self, sysid, description):

        payload = {"description": description}

        return self._patch_incident(sysid, payload)

    def update_urgency(self, sysid, urgency):

        payload = {"urgency": urgency}

        return self._patch_incident(sysid, payload)

    def add_work_notes(self, sysid, work_note):

        payload = {"work_notes": work_note}

        return self._patch_incident(sysid, payload)

    def add_customer_comments(self, sysid, comment):

        payload = {"comments": comment}

        return self._patch_incident(sysid, payload)

    def resolve_incident(
        self, sysid, resolution_code, resolution_notes, **extra_fields
    ):

        payload = {
            "state": "6",
            "close_code": resolution_code,
            "close_notes": resolution_notes,
        }
        payload.update(extra_fields)
        return self._patch_incident(sysid, payload)
