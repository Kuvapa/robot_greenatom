from fastapi import FastAPI

from robot import robot_count, switch_count


app = FastAPI(title='Robot_greenatom')

@app.post("/start")
async def start_endpoint(start_point: int = 0):
    await switch_count(False)
    await robot_count(start_point)
    return {"message": "Robot started with initial value set to: " + str(
            start_point)}


@app.post("/stop")
async def stop_count_endpoint(bool_flag: bool = True):
    await switch_count(bool_flag)