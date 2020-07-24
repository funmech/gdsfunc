# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import flask
import pytest

import main


# Create a fake "app" for generating test request contexts.
@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)


def test_hello_no_args(app):
    with app.test_request_context():
        res = main.hello(flask.request)
        assert 'Hello World!' in res


def test_hello_get(app):
    with app.test_request_context(query_string={'name': 'test'}):
        res = main.hello(flask.request)
        assert 'Hello test!' in res


def test_hello_args(app):
    with app.test_request_context(json={'name': 'test'}):
        res = main.hello(flask.request)
        assert 'Hello test!' in res


def test_hello_empty_json(app):
    with app.test_request_context(json=''):
        res = main.hello(flask.request)
        assert 'Hello World!' in res


def test_hello_xss(app):
    with app.test_request_context(json={'name': '<script>alert(1)</script>'}):
        res = main.hello(flask.request)
        assert '<script>' not in res
