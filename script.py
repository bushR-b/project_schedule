# объявление import
from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
import random
import uvicorn

# инициализация
app = FastAPI()

# монтирование статической папки для обслуживания статических файлов
app.mount("/static/", StaticFiles(directory="static"), name="static")

# экземпляр шаблона Jinja2 для возврата веб-страниц через шаблонизатор
templates = Jinja2Templates(directory="templates")
days = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
subject = ("Математика","Русский, Окружающий Мир", "Русский", "Математика", "Окружающий Мир", "Математика", "Окружающий Мир")
time = ("12:30-13:30","13:30-14:30")

# hello world, метод GET, возврат строки

@app.get("/", response_class=HTMLResponse)
async def main_page():
    return templates.get_template("index.html").render({"days": days, "subjects": subject, "datas": time})

@app.get("/form", response_class=HTMLResponse)
async def form_page():
    return templates.get_template("form.html").render()