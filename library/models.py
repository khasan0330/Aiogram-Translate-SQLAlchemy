from sqlalchemy import String, BigInteger, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from library.configs import user, password, ipaddress, db_name

engine = create_engine(f"postgresql://{user}:{password}@{ipaddress}/{db_name}", echo=False)


class Base(DeclarativeBase):
    pass


class Translate(Base):
    __tablename__ = "translate_history"
    history_id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    src: Mapped[str] = mapped_column(String(30))
    dst: Mapped[str] = mapped_column(String(30))
    original_text: Mapped[str] = mapped_column(String)
    translate_text: Mapped[str] = mapped_column(String)

    def __str__(self):
        return f"User(id={self.history_id!r}, telegram_id={self.telegram_id!r}, " \
               f"src={self.src!r}, dst={self.dst!r}, original_text={self.original_text!r}, " \
               f"translate_text={self.translate_text!r},)"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
