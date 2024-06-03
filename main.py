from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import logging

folderName = "folder/"
app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 上传文件
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(folderName + file.filename, "wb") as f:
        f.write(file.file.read())
        logger.info("upload file")
        logger.info(file.file.name)
    logger.info("fileddd")
    return {"filename": file.filename}

# 下载文件
@app.get("/download/{file_path:path}")
async def download_file(file_path: str):
    path = Path(folderName + file_path)
    if not path.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path, filename=path.name)

if __name__ == "__main__":
    logger.info("file transfer start")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

