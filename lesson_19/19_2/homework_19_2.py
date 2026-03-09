import requests

BASE_URL = "http://127.0.0.1:8080"

def upload_image(path):
    with open(path, "rb") as img:
        files = {"image": img}
        response = requests.post(f"{BASE_URL}/upload", files=files)
    return response

def get_image(filename):
    response = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "text"})
    return response

def delete_image(filename):
    response = requests.delete(f"{BASE_URL}/delete/{filename}")
    return response