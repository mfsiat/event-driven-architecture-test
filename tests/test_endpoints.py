from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_thumbnail():
    source_url = 'sourceurl'
    response = client.post('/thumbnail', json={'url': source_url})
    assert response.status_code == 200
    assert response.json() != None

    output = response.json()
    assert output['url'] == source_url
    assert output['filename'] != None 
