import flask
import json

from gclient import DSClient


def hello(request):
    """A HTTP Cloud Function copied from GCP doc - https://github.com/GoogleCloudPlatform/python-docs-samples.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}! from {}'.format(flask.escape(name), flask.__version__)


def list(_):
    ds_client = DSClient()
    kinds = ds_client.list_kinds(False)
    if len(kinds) > 0:
        return json.dumps(ds_client.get_keys(kinds[0])), 200, {'content-type': 'application/json'}
    return json.dumps([]), 200, {'content-type': 'application/json'}
