from app import app

def test_hello():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'From the moment I met you, my world has never been the same' in res.data
    assert b'every heartbeat' in res.data
    assert b'lifetimes' in res.data
