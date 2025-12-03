from dataclasses import dataclass
from datetime import datetime


@dataclass
class MessageItem:
    msg_id: int
    channel_name: str
    channel_id: int
    author_name: str 
    author_id: int 
    text: str 
    date: datetime | None
    raw: object