from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from threading import Thread

from app.core.config import settings
from app.scripts.robot import robot_count, switch_count


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


@app.post("/start")
async def start_endpoint(start_point: int = 0):
    th = Thread(target=await robot_count(), args=(start_point, ))
    await switch_count(False)
    th.start()
    return {"message": "Робот запущен со стартовым значением: " + str(
            start_point)}


@app.post("/stop")
async def stop_count_endpoint(bool_flag: bool = True):
    await switch_count(bool_flag)