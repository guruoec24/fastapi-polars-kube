from fastapi import FastAPI, BackgroundTasks, HTTPException, Header
from etl import main as run_etl
from config import SECRET_TOKEN

app = FastAPI()

def run_etl_background():
    run_etl()

@app.post("/trigger-etl")
async def trigger_etl(background_tasks: BackgroundTasks, authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=403, detail="Unauthorized")

    background_tasks.add_task(run_etl_background)
    return {"message": "ETL has been triggered and is running in background."}
