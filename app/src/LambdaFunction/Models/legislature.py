from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import date


class Base(DeclarativeBase):
    pass

class Legislature(Base):
    __tablename__ = "legislatura"
    id: Mapped[int] = mapped_column(primary_key=True)
    uri: Mapped[str] = mapped_column(String(100))
    dataInicio: Mapped[date] = mapped_column(Date)
    dataFim: Mapped[date] = mapped_column(Date)