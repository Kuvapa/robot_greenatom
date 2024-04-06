import subprocess
import psutil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

process_in_work = None

@app.post("/start")
async def start_endpoint(start_point: int = 0):
    global process_in_work
    if process_in_work:
        return {"message": "Робот уже запущен"}
    process_in_work = subprocess.Popen(
        ["start", "/WAIT", "./app/scripts/robot.py", f"{start_point}"],
        shell=True
    )
    return {"message": f"Робот запущен со стартовым значением: {start_point}"}


@app.post("/stop")
async def stop_count_endpoint():
    global process_in_work
    if not process_in_work:
        return {"message": "Робот не запущен"}
    process_pid = process_in_work.pid
    psutil.Process(process_pid).children()[0].kill()
    process_in_work = None
    return {"message": "Робот остановлен"}