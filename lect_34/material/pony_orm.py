from pony import orm


db = orm.Database()


class User(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    photos = orm.Set('Photo')
    age = orm.Required(int)


class Photo(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    url = orm.Required(str)
    owner = orm.Required(User)
    tags = orm.Set('Tag')


class Tag(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    photos = orm.Set(Photo)


db.bind(provider='sqlite', filename='testDB3.db', create_db=True)
db.generate_mapping(create_tables=True)
orm.set_sql_debug(True)
######################
@orm.db_session
def fill_data():
    u1 = User(name='Alice', age=17)
    u2 = User(name='Bob', age=18)
    p1 = Photo(url='https://www.pinterest.com/pin/706080047826475767/', owner=u1)
    p2 = Photo(url='https://900913.ru/static/img/logo-192x192.png', owner=u2)
    p3 = Photo(url='https://900913.ru/static/img/9cover.jpg', owner=u2)
    orm.commit()

    print(orm.select(p.url for p in Photo if p.owner == u1)[:10])
    print([p.url for p in u2.photos])
    print(orm.select(u.name for u in User if u.age >= 18)[:10])

#fill_data()

@orm.db_session
def create_select_m2m():
    t1 = Tag(name='sql')
    t2 = Tag(name='linux')
    t3 = Tag(name='python')

    for p in orm.select(x for x in Photo):
        if p.id % 2:
            p.tags.add(t1)
            p.tags.add(t2)
        else:
            p.tags.add(t2)

    print(orm.select(p.url for p in Photo if t1 in p.tags)[:])

create_select_m2m()

