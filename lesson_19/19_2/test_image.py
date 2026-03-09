from pathlib import Path
from homework_19_2 import *

def test_upload_get_delete():
    image_path = Path(__file__).parent / "example.jpg"

    response = upload_image(image_path)
    assert response.status_code == 201

    data = response.json()
    image_url = data["image_url"]
    filename = image_url.split("/")[-1]

    response = get_image(filename)
    assert response.status_code == 200

    response = delete_image(filename)
    assert response.status_code == 200

