from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

tags = Table('tag_image', Base.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id')),
    Column('image_id', Integer, ForeignKey('images.id'))
)

class Image(Base):

    __tablename__ = 'images'

    id          =   Column(Integer, primary_key=True)
    uuid        =   Column(String(36), unique=True, nullable=False)
    likes       =   Column(Integer, default=0)
    created_at  =   Column(DateTime, default=datetime.utcnow)
    tags        =   relationship('Tag', secondary=tags, 
                        backref = backref('images', lazy='dynamic'))
    comments    =   relationship('Comment', backref='image', lazy='dynamic')

    def __repr__(self):
        str_created_at = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return "<Image (uuid='%s', likes='%d', created_at=%s)>" % (self.uuid, self.likes, str_created_at)

class Tag(Base):

    __tablename__ = 'tags'

    id      =   Column(Integer, primary_key=True)
    name    =   Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<Tag (name='%s')>" % (self.name)

class Comment(Base):

    __tablename__ = 'comments'

    id          =   Column(Integer, primary_key=True)
    text        =   Column(String(2000))
    image_id    =   Column(Integer, ForeignKey('images.id'))

    def __repr__(self):
        return "<Comment (text='%s')>" % (self.text)

#----------------------------
# Turn Foreign Key Constraints ON for
# each connection.
#----------------------------

from sqlalchemy.engine import Engine
from sqlalchemy import event

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

#----------------------------
# Create the engine
#----------------------------

from sqlalchemy import create_engine
engine = create_engine('sqlite:///sql_alchemy.db', echo=True)

#----------------------------
# Create the Schema
#----------------------------

Base.metadata.create_all(engine)

#----------------------------
# Create the Session class 
#----------------------------

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

#----------------------------
# Populate the database 
#----------------------------

tag_cool = Tag(name='cool')
tag_car = Tag(name='car')
tag_animal = Tag(name='animal')

comment_rhino = Comment(text='Rhinoceros, often abbreviated as rhino, is a group of five extant species of odd-toed ungulates in the family Rhinocerotidae.')

image_car = Image(uuid='uuid_car', \
    tags=[tag_car, tag_cool], \
    created_at=(datetime.utcnow() - timedelta(days=1)))

image_another_car = Image(uuid='uuid_anothercar', \
    tags=[tag_car])

image_rhino = Image(uuid='uuid_rhino', \
    tags=[tag_animal], \
    comments=[comment_rhino])

# Create a new Session and add the images:
session = Session()

session.add(tag_cool)
session.add(tag_car)
session.add(tag_animal)

session.add(comment_rhino)

session.add(image_car)
session.add(image_another_car)
session.add(image_rhino)

# Commit the changes:
session.commit()

#----------------------------
# Update a Record
#----------------------------

image_to_update = session.query(Image).filter(Image.uuid == 'uuid_rhino').first()
image_to_update.likes = image_to_update.likes + 1
session.commit()

#----------------------------
# Query the database
#
# List of common filter: 
#
#   *http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html#common-filter-operators
#
#----------------------------

# Get a list of tags:
for name in session.query(Tag.name).order_by(Tag.name):
    print (name)

# How many tags do we have?
session.query(Tag).count()

# Get all images created yesterday:
session.query(Image) \
    .filter(Image.created_at < datetime.utcnow().date()) \
    .all()

# Get all images, that belong to the tag 'car' or 'animal', using a subselect:
session.query(Image) \
    .filter(Image.tags.any(Tag.name.in_(['car', 'animal']))) \
    .all()

# This can also be expressed with a join:
session.query(Image) \
    .join(Tag, Image.tags) \
    .filter(Tag.name.in_(['car', 'animal'])) \
    .all()

# Play around with functions:
from sqlalchemy.sql import func, desc

max_date = session.query(func.max(Image.created_at))
session.query(Image).filter(Image.created_at == max_date).first()

# Get a list of tags with the number of images:
q = session.query(Tag, func.count(Tag.name)) \
    .outerjoin(Image, Tag.images) \
    .group_by(Tag.name) \
    .order_by(desc(func.count(Tag.name))) \
    .all()

for tag, count in q:
    print ('Tag "%s" has %d images.' % (tag.name, count)) 

# Get images created in the last two hours and zero likes so far:
session.query(Image) \
    .join(Tag, Image.tags) \
    .filter(Image.created_at > (datetime.utcnow() - timedelta(hours=2))) \
    .filter(Image.likes == 0) \
    .all()