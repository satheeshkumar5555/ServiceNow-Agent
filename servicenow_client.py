import requests
from config import INSTANCE, USERNAME, PASSWORD


class ServiceNowClient:

    def create_incident(self, short_description, description):


        url = f"{INSTANCE}/api/now/table/incident"

        payload = {
            "short_description": short_description,
            "description": description
        }

        response = requests.post(
            url,
            auth=(USERNAME, PASSWORD),
            json=payload,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )

        if response.status_code == 201:
         
            result = response.json()["result"]

        return result

        raise Exception(response.text)
    
    
    def get_incident(self, incident_number):


        url = f"{INSTANCE}/api/now/table/incident"
        params = {
            "sysparm_query": f"number={incident_number}",
            "sysparm_fields": "number,short_description,description,state"
        }
       
        response = requests.get(
            url,
            auth=(USERNAME, PASSWORD),
          params=params,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )

        if response.status_code == 200:
         result = response.json()["result"]

        if len(result) == 0:
         return None
        else:
            return result[0]

        raise Exception(response.text)
    
    