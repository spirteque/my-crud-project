from sqlmodel import Session, select

from .models import Item


def create_item(session: Session, item: Item) -> Item:
	session.add(item)
	session.commit()
	session.refresh(item)
	return item


def get_items(session: Session):
	return session.exec(select(Item)).all()


def delete_item(session: Session, item_id: int) -> bool:
	item = session.get(Item, item_id)
	if item:
		session.delete(item)
		session.commit()
		return True
	return False
