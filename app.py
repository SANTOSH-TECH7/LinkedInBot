from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from linkedin_hr_bot import run_bot

app = FastAPI()  # ✅ Don't forget this

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def submit(request: Request, username: str = Form(...), password: str = Form(...), keyword: str = Form(...)):
    result = run_bot(username, password, keyword)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
