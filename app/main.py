from fastapi import FastAPI
from app.config import settings 
from app.db import engine, SessionLocal, Base
from fastapi.responses import FileResponse
from datetime import datetime
import uvicorn
from app.router_users import router

def create_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app    

app = start_application()

app.include_router(router)

@app.on_event("startup")
def on_startup():
    with open("log_p.txt", mode="a") as log:
        log.write(f'{datetime.utcnow()}: Begin\n')

@app.on_event("shutdown")
def shutdown():
    with open("log_p.txt", mode="a") as log:
        log.write(f'{datetime.utcnow()}: End\n')

@app.get("/")
def main():
    return FileResponse("files/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
