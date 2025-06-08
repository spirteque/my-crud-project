from pathlib import Path

from fastapi import FastAPI, Depends, HTTPException, Request
from sqlmodel import Session
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from .crud import create_item, get_items, delete_item, create_person
from .database import init_db, get_session
from .models import Item, Person

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.on_event("startup")
def on_startup():
	init_db()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/items/", response_model=Item)
def add_item(item: Item, session: Session = Depends(get_session)):
	if item.name == "forbidden":
		raise HTTPException(status_code=409)
	return create_item(session, item)


@app.get("/api/items/", response_model=list[Item])
def read_items(session: Session = Depends(get_session)):
	return get_items(session)


@app.delete("/api/items/{item_id}")
def remove_item(item_id: int, session: Session = Depends(get_session)):
	success = delete_item(session, item_id)
	if not success:
		raise HTTPException(status_code=404, detail="Item not found")
	return {"ok": True}


@app.get("/api/cool_items/", response_model=list[Item])
def read_items(session: Session = Depends(get_session)):
	return get_items(session)


@app.post("/api/persons/", response_model=Person)
def add_item(person: Person, session: Session = Depends(get_session)):
	return create_person(session, person)
