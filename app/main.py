from fastapi import FastAPI, Depends, HTTPException, Request
from sqlmodel import Session
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from .crud import create_item, get_items, delete_item
from .database import init_db, get_session
from .models import Item

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
def on_startup():
	init_db()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})


@app.post("/items/", response_model=Item)
def add_item(item: Item, session: Session = Depends(get_session)):
	return create_item(session, item)


@app.get("/items/", response_model=list[Item])
def read_items(session: Session = Depends(get_session)):
	return get_items(session)


@app.delete("/items/{item_id}")
def remove_item(item_id: int, session: Session = Depends(get_session)):
	success = delete_item(session, item_id)
	if not success:
		raise HTTPException(status_code=404, detail="Item nto found")
	return {"ok": True}
