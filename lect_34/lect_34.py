# from datetime import datetime
#
# from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, \
#     SmallInteger, and_, or_, not_
# from sqlalchemy import Boolean, PrimaryKeyConstraint, UniqueConstraint, ForeignKeyConstraint
# from sqlalchemy.orm import declarative_base, relationship, Session
#
# # engine = create_engine('mysql+pymysql://login:pass@localhost/mydb')
# # engine = create_engine('mysql+mysqldb://login:pass@25.32.113.45/mydb')
#
# engine = create_engine('sqlite:///my_sqlite_db.db')
# engine.connect()
#
# Base = declarative_base()
#
#
# class Customer(Base):
#     __tablename__ = 'customers'
#     id = Column(Integer(), primary_key=True)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     email = Column(String(100), nullable=False)
#     orders = relationship('Order', backref='customer')
#
# class Item(Base):
#     __tablename__ = 'items'
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(100), nullable=False)
#     cost_price = Column(Numeric(10, 2), nullable=False)
#     selling_price = Column(Numeric(10, 2), nullable=False)
#     quantity = Column(Integer())
#
# class Order(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer(), primary_key=True)
#     customer_id = Column(Integer(), ForeignKey('customers.id'))
#     item_id = Column(Integer(), ForeignKey('items.id'))
#     date_placed = Column(DateTime(), default=datetime.now)
#     line_items = relationship('OrderLine', backref='order')
#
# class OrderLine(Base):
#     __tablename__ = 'order_lines'
#     id = Column(Integer(), primary_key=True)
#     order_id = Column(Integer(), ForeignKey('orders.id'))
#     item_id = Column(Integer(), ForeignKey('items.id'))
#     quantity = Column(SmallInteger())
#     item = relationship('Item')
#
# Base.metadata.create_all(engine)
# session = Session(bind=engine)
#
# c1 = Customer(
#     first_name = 'Dmitriy',
#     last_name = 'Yatsenko',
#     email = 'moseend@mail.com'
# )
# c2 = Customer(
#     first_name = 'Valeriy',
#     last_name = 'Golyshkin',
#     email = 'fortioneaks@gmail.com'
# )
# c3 = Customer(
#     first_name = "Vadim",
#     last_name = "Moiseenko",
#     email = "antence73@mail.com",
# )
# c4 = Customer(
#     first_name = "Vladimir",
#     last_name = "Belousov",
#     email = "andescols@mail.com",
# )
# c5 = Customer(
#     first_name = "Tatyana",
#     last_name = "Khakimova",
#     email = "caltin1962@mail.com",
# )
# c6 = Customer(
#     first_name = "Pavel",
#     last_name = "Arnautov",
#     email = "lablen@mail.com",
# )
#
# # session.add_all([c1, c2, c3, c4, c5, c6])
# # session.commit()
#
# i1 = Item(name = 'Chair', cost_price = 9.21, selling_price = 10.81, quantity = 5)
# i2 = Item(name = 'Pen', cost_price = 3.45, selling_price = 4.51, quantity = 3)
# i3 = Item(name = 'Headphone', cost_price = 15.52, selling_price = 16.81, quantity = 50)
# i4 = Item(name = 'Travel Bag', cost_price = 20.1, selling_price = 24.21, quantity = 50)
# i5 = Item(name = 'Keyboard', cost_price = 20.1, selling_price = 22.11, quantity = 50)
# i6 = Item(name = 'Monitor', cost_price = 200.14, selling_price = 212.89, quantity = 50)
# i7 = Item(name = 'Watch', cost_price = 100.58, selling_price = 104.41, quantity = 50)
# i8 = Item(name = 'Water Bottle', cost_price = 20.89, selling_price = 25, quantity = 50)
#
# # session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
# # session.commit()
#
# o1 = Order(customer = c1)
# o2 = Order(customer = c1)
#
# line_item1 = OrderLine(order=o1, item = i1, quantity = 3)
# line_item2 = OrderLine(order=o1, item = i2, quantity = 2)
# line_item3 = OrderLine(order=o2, item = i1, quantity = 1)
# line_item4 = OrderLine(order=o2, item = i2, quantity = 4)
#
# # session.add_all([o1, o2])
# # session.commit()
# ##############
# #print(session.query(Customer.first_name).all())
# #print(session.query(Customer.first_name))
#
# # print(session.query(Customer.first_name, Order.line_items).join(Order, Order.customer_id == Customer.id).all())
#
# # q = session.query(Customer)
# #
# # for i in q:
# #     print(i.id, i.first_name)
#
# # print(session.query(Item).count())
# #
# # print(session.query(Item.name).first())
#
# # print(session.query(Customer.last_name).filter(Customer.first_name == 'Vadim', Customer.id < 5))
#
# # print(session.query(Customer.last_name).limit(3).all())
#
# # print(session.query(Item.name, Item.quantity).filter(Item.cost_price.between(10, 50)).all())
# # print()
# # print(session.query(Item.name, Item.quantity).filter(not_(Item.cost_price.between(10, 50))).all())
#
# # print(session.query(Customer.first_name).join().all())
#
# # i = session.query(Item).first()
# #
# # i.selling_price = 2598.85
# # session.add(i)
# # session.commit()
# #
# # print(session.query(Item.name, Item.selling_price).all())
#
# # i = session.query(Item).filter(Item.cost_price == 3.45).one()
# #
# #
# # session.delete(i)
# # session.commit()
# #
# # print(session.query(Item.name, Item.cost_price).all())
#
#
#
# from pony import orm
#
# db = orm.Database()
#
# class User(db.Entity):
#     id = orm.PrimaryKey(int, auto=True)
#     name = orm.Required(str)
#     photos = orm.Set('Photo')
#     age = orm.Required(int)
#
# class Photo(db.Entity):
#     id = orm.PrimaryKey(int, auto=True)
#     url = orm.Required(str)
#     owner = orm.Required(User)
#     tags = orm.Set('Tag')
#
# class Tag(db.Entity):
#     id = orm.PrimaryKey(int, auto=True)
#     name = orm.Required(str)
#     photos = orm.Set(Photo)
#
#
# db.bind(provider='sqlite', filename='database_pony.db', create_db=True)
# db.generate_mapping(create_tables=True)
# orm.set_sql_debug(True)
# #####
# @orm.db_session
# def fill_data():
#     u1 = User(name='Alice', age=17)
#     u2 = User(name='Bob', age=18)
#     p1 = Photo(url='https://www.pinterest.com/pin/700802392041934450/', owner=u1)
#     p2 = Photo(url='https://www.pinterest.com/pin/700802392037530502/', owner=u2)
#     p3 = Photo(url='https://www.pinterest.com/pin/700802392005718776/', owner=u2)
#     orm.commit()
#     print(orm.select(p.url for p in Photo if p.owner == u1)[:10])
#
# fill_data()
#
# # @orm.db_session
# # def select_data():
# #     print(orm.select(p.url for p in Photo))

import pymongo

my_client = pymongo.MongoClient('mongodb://localhost:27017/')

my_db = my_client['my_database']

my_col = my_db['customers']

my_d = {'name': 'J', 'addr': 'psd'}

x = my_col.insert_one(my_d)
