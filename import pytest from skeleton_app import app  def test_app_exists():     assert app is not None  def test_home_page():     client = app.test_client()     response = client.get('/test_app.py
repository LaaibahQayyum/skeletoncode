import pytest
from skeleton_app import app

def test_app_exists():
    assert app is not None

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello' in response.data  # Adjust based on your actual response

# Add more tests as needed
