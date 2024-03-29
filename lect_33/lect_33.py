from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, \
    SmallInteger
from sqlalchemy import Boolean, PrimaryKeyConstraint, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base, relationship, Session

# engine = create_engine('mysql+pymysql://login:pass@localhost/mydb')
# engine = create_engine('mysql+mysqldb://login:pass@25.32.113.45/mydb')

engine = create_engine('sqlite:///my_sqlite_db.db')
engine.connect()

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    orders = relationship('Order', backref='customer')

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer())

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship('OrderLine', backref='order')

class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship('Item')

Base.metadata.create_all(engine)
session = Session(bind=engine)

c1 = Customer(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko',
    email = 'moseend@mail.com'
)
c2 = Customer(
    first_name = 'Valeriy',
    last_name = 'Golyshkin',
    email = 'fortioneaks@gmail.com'
)
c3 = Customer(
    first_name = "Vadim",
    last_name = "Moiseenko",
    email = "antence73@mail.com",
)
c4 = Customer(
    first_name = "Vladimir",
    last_name = "Belousov",
    email = "andescols@mail.com",
)
c5 = Customer(
    first_name = "Tatyana",
    last_name = "Khakimova",
    email = "caltin1962@mail.com",
)
c6 = Customer(
    first_name = "Pavel",
    last_name = "Arnautov",
    email = "lablen@mail.com",
)

# session.add_all([c1, c2, c3, c4, c5, c6])
# session.commit()

i1 = Item(name = 'Chair', cost_price = 9.21, selling_price = 10.81, quantity = 5)
i2 = Item(name = 'Pen', cost_price = 3.45, selling_price = 4.51, quantity = 3)
i3 = Item(name = 'Headphone', cost_price = 15.52, selling_price = 16.81, quantity = 50)
i4 = Item(name = 'Travel Bag', cost_price = 20.1, selling_price = 24.21, quantity = 50)
i5 = Item(name = 'Keyboard', cost_price = 20.1, selling_price = 22.11, quantity = 50)
i6 = Item(name = 'Monitor', cost_price = 200.14, selling_price = 212.89, quantity = 50)
i7 = Item(name = 'Watch', cost_price = 100.58, selling_price = 104.41, quantity = 50)
i8 = Item(name = 'Water Bottle', cost_price = 20.89, selling_price = 25, quantity = 50)

# session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
# session.commit()

o1 = Order(customer = c1)
o2 = Order(customer = c1)







# user_post = Table('user_post', Base.metadata,
#     Column('user_id', Integer(), ForeignKey('users.id')),
#     Column('post_id', Integer(), ForeignKey('posts.id'))
# )
#
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer(), primary_key=True)
#     username = Column(String(100), nullable=False)
#     email_user = Column(String(100), nullable=False)
#     password = Column(String(100), nullable=False)
#     posts = relationship('Post', backref='person')
#
#     __table_tags__ = (
#         PrimaryKeyConstraint('id', name='user_pk'),
#         UniqueConstraint('username', 'email_user')
#     )
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer(), primary_key=True)
#     title = Column(String(100), nullable=False)
#     slug = Column(String(100), nullable=False, unique=True)
#     content = Column(String(200), nullable=False)
#     user_id = Column(Integer())
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#     author = relationship('User')
#
#     __table_tags__ = (
#         ForeignKeyConstraint(['user_id'], ['users.id'])
#     )



# Base.metadata.create_all(engine)