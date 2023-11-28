import json
import pytest
from app import app, read_users_from_file, write_user_to_file

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.post('/', data=dict(username='1', password='1'))
    assert response.status_code == 302  # Redirect status code

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200  # OK status code
    assert b'About Page' in response.data

def test_home_page(client):
    response = client.get('/home')
    assert response.status_code == 200  # OK status code
    assert b'Home Page' in response.data

def test_register_existing_user(client):
    response = client.post('/register', data=dict(username='1', password='1'))
    assert b'Username already exists' in response.data


def test_register_new_user(client):
    response = client.post('/register', data=dict(username='19', password='19'))
    assert response.status_code == 400  # Redirect status code

    # Additional assertion to check if the new user is in the file
    users = read_users_from_file()
    assert any(user['username'] == '19' for user in users)

    # Clean up, remove the newly registered user from the file
    users = [user for user in users if user['username'] != '19']
    with open('users.json', 'w') as file:
        json.dump({'users': users}, file)
