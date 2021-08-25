from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import todo

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/today")
def get_today(request: Request):
    return templates.TemplateResponse("today.html", {"request":request, "items": todo.get_items()})


if __name__ == '__main__':
    uvicorn.run("app:app", port=5000)
    print(f"Kicked off.")

# TODO - Add Endpoint to handle Task Complete Order
# TODO - Dockerize It
# TODO - Add FastAPI Utils or add a way to refresh screen every minute.
