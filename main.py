from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# 上传文件
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open("folder/" + file.filename, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}

# 下载文件
@app.get("/download/{file_path:path}")
async def download_file(file_path: str):
    path = Path("folder/" + file_path)
    if not path.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path, filename=path.name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

