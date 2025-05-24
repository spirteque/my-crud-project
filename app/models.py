from typing import Optional

from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
	description: Optional[str] = None

