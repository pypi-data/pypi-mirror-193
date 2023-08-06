import json
import requests

def error_handler(resource):
    print(f"Status: {response.status_code}")
    print(f"ErrorMessage: {response.json()['error']}")
    return {response.json()['error']}

def getResource():
    url = "http://quantum-resource.qcc.svc.cluster.local:8080"
    url_path = f"{url}/v1/resources"

    params = {
        "page": -1,
        "size": 0
    }

    response = requests.get(f"{url_path}", params=params)
    
    if response.status_code != 200:
        return error_handler(response)

    data = json.loads(response.content)
    print("{:<40} {:<15} {:<10} {:<10} {:<10}".format("id", "name", "type", "status", "qubits"))
    for vals in data["resources"]:
        print("{:<40} {:<15} {:<10} {:<10} {:<10}".format(vals["id"], vals["name"], vals["type"], vals["status"], vals["qubits"]))

    return response.text

def getResourceName(resourceId):
    url = "http://job-management.qcc.svc.cluster.local:8080"
    url_path = f"{url}/v1/resources/{resourceID}"

    response = requests.get(f"{url_path}") # , params=params)
    
    if response.status_code != 200:
        return error_handler(response)

    data = json.loads(response.content)
    return data["name"]