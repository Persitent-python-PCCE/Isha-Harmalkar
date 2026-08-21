


def test_register(client):
    response  = client.post(
        "/register",
        data={
            "name": "John",
            "email": "john@test.com",
            "password": "password123",
            "confirm_password": "password123"
        }

    )

    assert response.status_code == 302


def test_login(client):
    client.post(
        "/register",
        data={
            "name": "John",
            "email": "john@test.com",
            "password": "password123",
            "confirm_password": "password123"
        }

    )

    response = client.post(
        "/login",
        data={
            "email": "john@test.com",
            "password": "password123"
        }
    )


def test_invalid_login(client):
    response  = client.post(
        "/login",
        data={
            "email": "doestnotexist@test.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200


