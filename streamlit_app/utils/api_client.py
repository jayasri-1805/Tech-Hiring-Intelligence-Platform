import requests

BASE_URL = "http://127.0.0.1:8000"

def predict(payload):
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def health():
    response = requests.get(
        f"{BASE_URL}/health",
        timeout=10
    )

    response.raise_for_status()

    return response.json()