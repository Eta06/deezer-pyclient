from PIL import Image, ImageDraw, ImageOps
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
        name = user_info["name"]
        picture = user_info["picture"]
        country = user_info["country"]
        return name, picture, country
    else:
        print(f"Hata Kodu: {response.status_code}, Hata Mesajı: {response.text}")
        return None


def get_user_flow(session_token, user_id):
    api_url = f"https://api.deezer.com/user/{user_id}/flow"
    headers = {"Authorization": f"Bearer {session_token}"}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        user_flow = response.json()

        return user_flow
    else:
        print(f"Hata Kodu: {response.status_code}, Hata Mesajı: {response.text}")
        return None


def read_arl_token():
    """
    Reads arl token from app_config.json file
    :return: arl token
    """
    try:
        with open("app_config.json", "r", encoding="utf-8") as f:
            arl_token = json.load(f)["arl_token"]
            language = json.load(f)["language"]
            theme = json.load(f)["theme"]
    except FileNotFoundError:
        with open("app_config.json", "w", encoding="utf-8") as f:
            json.dump({"arl_token": "", "language": "en", "theme": "dark"}, f, indent=4)
        arl_token = False
        language = "en"
        theme = "dark"
    except:
        with open("app_config.json", "w", encoding="utf-8") as f:
            json.dump({"arl_token": "", "language": "en", "theme": "dark"}, f, indent=4)
        arl_token = False
        language = "en"
        theme = "dark"
    return arl_token, language, theme


def init():
    arl_token, language, theme = read_arl_token()
    if not arl_token:
        print("arl_token bulunamadı")
    session_token, user_id = authenticate_user(arl_token)
    playlists = get_user_playlists(session_token, user_id)
    username, user_picture, country = get_user_info(session_token, user_id)

    # Download user picture
    with open("./assets/user_picture.jpg", "wb") as f:
        f.write(requests.get(user_picture).content)

    image = Image.open("./assets/user_picture.jpg")
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    # Rounded corners
    draw.ellipse((0, 0) + image.size, fill=255)
    image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    # Save the image with rounded corners
    image.putalpha(mask)
    image.save("./assets/rounded_user_picture.png")

    return {
        "session_token": session_token,
        "user_id": user_id,
        "playlists": playlists,
        "username": username,
        "user_picture": user_picture,
        "country": country,
        "language": language,
        "theme": theme
    }
