import requests
import json


def authenticate_user(arl):
    url = "https://www.deezer.com/ajax/gw-light.php"

    headers = {
        "cookie": f"arl={arl}",
        "content-type": "application/json",
    }

    # Define API method, version, and token
    params = {
        "method": "deezer.ping",
        "api_version": "1.0",
        "api_token": ""
    }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        print(response.json())
        session_token = response.json()["results"]["SESSION"]
        user_id = response.json()["results"]["USER_ID"]
        return session_token, user_id
    else:
        print(f"Hata Kodu: {response.status_code}, Hata Mesajı: {response.text}")
        return None, None


def get_user_playlists(session_token, user_id):
    api_url = f"https://api.deezer.com/user/{user_id}/playlists"
    headers = {"Authorization": f"Bearer {session_token}"}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        playlists = response.json()["data"]
        return playlists
    else:
        print(f"Hata Kodu: {response.status_code}, Hata Mesajı: {response.text}")
        return None


def get_user_info(session_token, user_id):
    api_url = f"https://api.deezer.com/user/{user_id}"
    headers = {"Authorization": f"Bearer {session_token}"}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        print(f"Hata Kodu: {response.status_code}, Hata Mesajı: {response.text}")
        return None


def read_arl_token():
    """
    Reads arl token from app_config.json file
    :return: arl token
    """
    with open("app_config.json", "r", encoding="utf-8") as f:
        arl_token = json.load(f)["arl_token"]
    return arl_token
