from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session

from .crud import create_item, get_items, delete_item
from .database import init_db, get_session
from .models import Item


app = FastAPI()


@app.on_event("startup")
def on_startup():
	init_db()


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
		raise HTTPException(status_code=404, detail="Item not found")
	return {"ok": True}
