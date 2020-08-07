from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

template = Jinja2Templates("templates")
app = FastAPI()


@app.get("/")
def index(request: Request):
    """
    index route
    :param request: request object
    :return: rendered template
    """
    return template.TemplateResponse("index.html", {"request": request})


@app.get("/{file_name}")
def get_files(file_name: str):
    """
    download js and favicon
    :param file_name:  name of requested file
    :return: FastApi FileResponse
    """
    if file_name == "favicon.ico":
        return FileResponse(f"./templates/{file_name}", status_code=200)
    return FileResponse(f"./termynal/{file_name}", status_code=200)
