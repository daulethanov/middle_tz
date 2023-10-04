from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_send_email_success():
    payload = {
        "to": "recipient@example.com",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.post("/send_email", json=payload)
    assert response.status_code == 200
    assert response.json() == {"OK": "Send message"}


def test_send_email_invalid_email():
    payload = {
        "to": "invalid_email",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.post("/send_email", json=payload)
    assert response.status_code == 400
    assert "error validate email" in response.text


def test_send_email_invalid_subject():
    payload = {
        "to": "recipient@example.com",
        "subject": "Invalid int Subject",
        "message": "Test Message"
    }
    response = client.post("/send_email", json=payload)
    assert response.status_code == 400
    assert "error validate subject" in response.text


def test_send_email_invalid_message():
    payload = {
        "to": "recipient@example.com",
        "subject": "Test Subject",
        "message": "Invalid int Message"
    }
    response = client.post("/send_email", json=payload)
    assert response.status_code == 400
    assert "error validate message" in response.text