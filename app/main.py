from fastapi import FastAPI
from app.config import settings
from app.database import create_tables
from app.router_users import router as users_router
from datetime import datetime

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(users_router)
    return app    

app = start_application()

@app.on_event("startup")
def on_startup():
    create_tables()
    with open("log_p.txt", mode="a") as log:
        log.write(f'{datetime.utcnow()}: Begin\n')

@app.on_event("shutdown")
def shutdown():
    with open("log_p.txt", mode="a") as log:
        log.write(f'{datetime.utcnow()}: End\n')

@app.get("/")
def main():
    return {"message": "Hello, World!"}
