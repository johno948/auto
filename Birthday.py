import requests

def get_birthday(access_token):
    url = f"https://graph.facebook.com/v19.0/me?fields=birthday&access_token={access_token}"
    response = requests.get(url)
    data = response.json()
    return data.get("birthday", "Birthday data not available")


token = ""

print(get_birthday(token))
