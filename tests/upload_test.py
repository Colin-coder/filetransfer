import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
folderName = "folder/"

def test_upload_file():
    files = {'file': ('test.txt', 'Hello, World!', 'text/plain')}
    response = client.post("/upload/", files=files)
    assert response.status_code == 200
    assert response.json()["filename"] == "test.txt"
    assert os.path.exists("folder/test.txt")
    # os.remove(folderName + "test.txt")

def test_download_file():
    with open("test.txt", "w") as f:
        f.write("Hello, World!")
    
    response = client.get("/download/test.txt")
    assert response.status_code == 200
    # assert response.headers["content-type"] == "application/octet-stream"
    assert response.headers["content-disposition"] == "attachment; filename=\"test.txt\""
    assert response.content == b"Hello, World!"

    os.remove(folderName + "test.txt")
