from app import app

def test_hello():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'I tried to eat healthy' in res.data
    assert b'if laziness was an Olympic' in res.data
    assert b'd be too lazy to show ' in res.data
