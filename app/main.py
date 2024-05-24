from fastapi import FastAPI
from app.config import settings
from app.database import create_tables
from app.router_users import router as users_router
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(users_router)
    return app    

app = start_application()

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем Jinja2Templates
templates = Jinja2Templates(directory="templates")

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

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
