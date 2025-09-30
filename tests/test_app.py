from app import app

def test_hello():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b"Hello DevOps" in res.data
