from app import app

def test_hello():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'Aniket' in res.data
    assert b'DevOps' in res.data
    assert b'Cybersecurity' in res.data
