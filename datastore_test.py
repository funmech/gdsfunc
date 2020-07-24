import flask
import json
import pytest
import os

import main


# Create a fake "app" for generating test request contexts.
@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)


@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") == "true", reason="Not able to setup emulator, so skip test_list")
def test_list(app):
    # need datastore emulator
    with app.test_request_context():
        res = main.list(flask.request)
        data = json.loads(res)
        assert isinstance(data, list)
