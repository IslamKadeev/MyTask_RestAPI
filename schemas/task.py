from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str
    description: str
    duedate: Optional[datetime]
