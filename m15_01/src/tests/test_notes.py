import os

import pytest
from fastapi.testclient import TestClient

import app

client = TestClient(app.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Notes APP v1.0"}


# @pytest.fixture
# def env_app():
#     return os.environ.get("ENV_APP")


def test_login_right():
    response = client.post(
        "/token", data={"username": "krabat@ex.ua", "password": "567234"}
    )
    assert response.status_code == 200
    r = response.json()
    token_type = r["token_type"]
    assert token_type == "bearer"


def test_login_wrong():
    response = client.post(
        "/token", data={"username": "krabat@meta.ua", "password": "567234"}
    )
    assert response.status_code == 401


def test_login_wrong_validation():
    response = client.post("/token", data={"username": "krabat@meta.ua"})
    assert response.status_code == 422


@pytest.fixture
def token(scope="module"):
    response = client.post(
        "/token", data={"username": "krabat@ex.ua", "password": "567234"}
    )
    return response.json()["access_token"]


def get_notes(token, capsys):
    response = client.get("/api/notes", headers={"Authorization": f"Bearer {token}"})
    data = response.json()
    with capsys.disabled():
        print("-------------")
        print(data)

    assert response.status_code == 200
    assert len(data) > 0
