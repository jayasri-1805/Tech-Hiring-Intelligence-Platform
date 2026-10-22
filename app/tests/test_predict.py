from .conftest import client

payload = {
    "experience_level":"Mid",
    "company_category":"Technology",
    "country":"India",
    "remote_category":"Remote"
}

def test_predict_endpoint():
    response = client.post("/predict", json=payload)
    assert response.status_code in (200,503)
