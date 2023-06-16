import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True, nullable=False)

    book = relationship("Book", back_populates="publisher")


class Book(Base):
    __tablename__ = "book"
    book_id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=64), unique=True, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey(
        "publisher.publisher_id"))

    publisher = relationship("Publisher", back_populates="book")
    stock = relationship("Stock", back_populates="book")


class Shop(Base):
    __tablename__ = "shop"
    shop_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=64), unique=True, nullable=False)

    stock = relationship("Stock", back_populates="shop")


class Sale(Base):
    __tablename__ = "sale"
    sale_id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.stock_id"))

    stock = relationship("Stock", back_populates="sale")


class Stock(Base):
    __tablename__ = "stock"
    stock_id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.book_id"))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.shop_id"))
    count = sq.Column(sq.Integer, nullable=False)

    shop = relationship("Shop", back_populates="stock")
    sale = relationship("Sale", back_populates="stock")
    book = relationship("Book", back_populates="stock")


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
