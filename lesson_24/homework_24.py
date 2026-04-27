import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    logger.info("Start authentication...")

    response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))

    assert response.status_code == 200

    access_token = response.json()["access_token"]

    session.headers.update({"Authorization": f"Bearer {access_token}"})

    logger.info("Token successfully extracted")

    return session

@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 4),
        ("price", 10),
        ("year", 1),
    ]
)
class TestCarsSearch:

    def test_get_cars(self, auth_session, sort_by, limit):

        logger.info(f"GET /cars sort_by={sort_by}, limit={limit}")

        params = {
            "sort_by": sort_by,
            "limit": limit
        }

        response = auth_session.get(f"{BASE_URL}/cars", params=params)

        logger.info(f"Status code: {response.status_code}")

        assert response.status_code == 200

        data = response.json()

        logger.info(f"Received {len(data)} records")

        assert len(data) <= limit

        for car in data:
            assert "brand" in car
            assert "year" in car
            assert "engine_volume" in car
            assert "price" in car