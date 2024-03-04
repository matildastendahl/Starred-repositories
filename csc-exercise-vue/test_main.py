import pytest
from fastapi.testclient import TestClient
from main import fetch_starred, render_html
from main import app

client = TestClient(app)

def test_login():
    response = client.get("/")
    assert response.status_code == 200
    assert "Login with GitHub" in response.text

def test_invalid_callback():
    response = client.get("/callback")
    assert response.status_code == 422

