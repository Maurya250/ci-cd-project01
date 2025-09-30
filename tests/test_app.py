from app import app

def test_hello():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'I see you every ' in res.data
    assert b'my heart races' in res.data
    assert b'is the loudest way my feelings ' in res.data
