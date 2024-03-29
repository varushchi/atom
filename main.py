from fastapi import FastAPI, Request, HTTPException
import asyncio

app = FastAPI()

robot_task = None

@app.post("/start_robot")
async def start_robot(request: Request):
    global robot_task

    if robot_task is not None:
        raise HTTPException(status_code=400, detail="Робот уже запущен")

    async def robot():
        i = 0
        while True:
            print(i)
            i += 1
            await asyncio.sleep(1)

    robot_task = asyncio.create_task(robot())
    return {"message": "Робот запущен"}

@app.post("/stop_robot")
async def stop_robot(request: Request):
    global robot_task

    if robot_task is None:
        raise HTTPException(status_code=400, detail="Робот не запущен")

    robot_task.cancel()
    robot_task = None
    return {"message": "Робот остановлен"}


if __name__ == "__main__":
    print("Starting FastAPI server...")
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
