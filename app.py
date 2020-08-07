from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

template = Jinja2Templates("templates")
app = FastAPI()


@app.get("/")
def index(request: Request):
    return template.TemplateResponse('index.html', {'request': request})


@app.get("/{file_name}")
def get_files(file_name):
    if file_name == 'favicon.ico':
        return FileResponse(f"./templates/{file_name}", status_code=200)
    return FileResponse(f"./termynal/{file_name}", status_code=200)
