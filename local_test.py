import server


def test_index():
    server.app.testing = True
    client = server.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
    assert 'Hello World' in r.data.decode('utf-8')
