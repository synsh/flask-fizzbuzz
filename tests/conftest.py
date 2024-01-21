import pytest
from fizzbuzz.db import get_db
from fizzbuzz import create_app

@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
