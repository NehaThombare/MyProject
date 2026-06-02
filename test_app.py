import pytest
from app import app

@pytest.fixture
def client():
    # Creates a temporary test client of our Flask app
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test that the main root route returns a 200 OK and correct message"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Microservice is running smoothly!" in response.data

def test_health_endpoint(client):
    """Test that the health check route returns a 200 OK and UP status"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data