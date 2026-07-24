from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

import matplotlib.pyplot as plt

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/output",
    StaticFiles(directory="output"),
    name="output"
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"image": None},
    )


@app.post("/plot", response_class=HTMLResponse)
def plot(
    request: Request,
    numbers: str = Form(...)
):

    values = list(map(float, numbers.split()))

    plt.figure(figsize=(6,4))

    plt.plot(values, marker="o")

    plt.grid(True)

    plt.savefig("output/plot.png")

    plt.close()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "image": "/output/plot.png"
        },
    )
@app.get("/square/{number}")
def square(number:int):
    return {
        "result":number*number
    }
