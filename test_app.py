import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if the homepage loads successfully and contains a joke"""
    response = client.get("/")
    assert response.status_code == 200  # Check if page loads correctly
    assert b"Random Joke Generator" in response.data  # Check if title is in response
    assert b"<p class=\"joke\">" in response.data  # Check if a joke is present
