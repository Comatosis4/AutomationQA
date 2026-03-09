import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q" : "Curiosity rover Mars",
    "media_type" : "image",
    "page_size" : 20
}

response = requests.get(search_url, params = search_params)
data = response.json()
items = data["collection"]["items"]

nasa_ids = []
for item in items:
    nasa_ids.append(item["data"][0]["nasa_id"])

jpg_urls = []
for nasa_id in nasa_ids[:2]:
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    asset_response = requests.get(asset_url)
    asset_data = asset_response.json()
    files = asset_data["collection"]["items"]
    for file in files:
        url = file["href"]
        if url.lower().endswith(".jpg"):
            jpg_urls.append(url)
            break

for i in range(len(jpg_urls)):
    filename = f"mars_photo{i}.jpg"
    img = requests.get(jpg_urls[i])

    with open(filename, "wb") as f:
        f.write(img.content)

