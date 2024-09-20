from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    orders = relationship('Order', back_populates='user')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)

    orders = relationship('Order', back_populates='product')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    order_date = Column(Date, default=datetime.datetime.utcnow)

    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')

# Create the database
def create_db():
    # Replace 'username', 'password', and 'grocery_store' with your actual credentials and database name
    engine = create_engine('postgresql://username:password@localhost/grocery_store')
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_db()
