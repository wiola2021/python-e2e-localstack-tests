import pytest
import requests
from api.post_sign_up import SignUp
from generators.user_generator import get_random_user


@pytest.fixture
def sign_up_api():
    return SignUp()


def test_successful_api_signup(sign_up_api: SignUp):
    user = get_random_user()
    response = sign_up_api.api_call(user)
    assert response.status_code == 201, "Expected status code 201"
    assert response.json().get("token") is not None, "Token should not be None"


def test_should_return_400_if_password_too_short(sign_up_api: SignUp):
    user = get_random_user()
    user.password = "123"  # intentionally short password
    try:
        response = sign_up_api.api_call(user)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 400, "Expected status code 400"
        assert (
            "password length" in e.response.json()["password"]
        ), "Password error should mention length"


def test_should_return_400_if_invalid_email_format(sign_up_api: SignUp):
    user = get_random_user()
    user.email = "invalid-email-format"
    try:
        response = sign_up_api.api_call(user)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 400, "Expected status code 400"
        assert (
            "email" in e.response.json()
        ), "Email error should be present in the response body"
        assert (
            "must be a well-formed email address" in e.response.json()["email"]
        ), "Error message should mention well-formed email address"


def test_should_return_422_if_email_already_exists(sign_up_api: SignUp):
    user = get_random_user()
    user.email = "heatherharrison@example.com"
    try:
        response = sign_up_api.api_call(user)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 422, "Expected status code 422"
        assert (
            "email" in e.response.json()
        ), "Email error should be present in the response body"
        assert (
            "already exists" in e.response.json()["email"]
        ), "Error message should mention email already exists"


