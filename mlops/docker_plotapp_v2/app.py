from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from plotting import create_plot

from config import UPLOAD_DIR


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/uploads",
    StaticFiles(directory=UPLOAD_DIR),
    name="uploads",
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"image": None},
    )


@app.post("/plot", response_class=HTMLResponse)
def plot_numbers(
    request: Request,
    numbers: str = Form(...)
):
    values = [int(x) for x in numbers.split()]

    image = create_plot(values)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "image": image
        },
    )
