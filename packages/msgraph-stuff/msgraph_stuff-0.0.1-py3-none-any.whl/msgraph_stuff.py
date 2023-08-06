import requests

def get_access_token(dir_id:str, app_id:str, secret_id:str): #return access_token
    """ must be registered as a web app in azure ad """

    url = f"https://login.microsoft.com/{dir_id}/oauth2/token"

    body = {
        "grant_type":"client_credentials",
        "client_id":app_id,
        "client_secret":secret_id,
        "resource":"https://graph.microsoft.com"
    }

    r = requests.post(url, data=body)
    
    if r.status_code not in range(200, 299):
        raise Exception(f"Could not authenticate client. Status code: {r.status_code}. Response: {r.text}")
    
    access_token = r.json()['access_token']
    return access_token

def standardGetRequest(token:str, endpoint:str, version:str="v1.0"):
    """ returns a response object """
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = f"https://graph.microsoft.com/{version}/{endpoint}"

    r = requests.get(url, headers=headers)

    return r