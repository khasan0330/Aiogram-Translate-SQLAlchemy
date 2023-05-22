from typing import Iterable
from sqlalchemy.orm import Session
from library.models import *


with Session(engine) as session:
    db_session = session


def db_history_write(chat_id: int, src: str, dst: str, text: str, finish_text: str) -> None:
    """Функция для записи истории переводов пользователя"""
    query = Translate(
        telegram_id=chat_id,
        src=src,
        dst=dst,
        original_text=text,
        translate_text=finish_text
    )
    db_session.add(query)
    db_session.commit()


def db_history_read(chat_id: int) -> Iterable:
    """Функция для чтения истории переводов пользователя"""
    query = select(Translate).where(Translate.telegram_id == chat_id).limit(5)
    histories: Iterable[Translate] = db_session.scalars(query)
    return histories
