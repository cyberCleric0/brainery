from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column

# Data Types to Import - Importing everything at first, clean up to keep
# Only the ones used.
from sqlalchemy import SmallInteger, Integer, BigInteger, Text, LargeBinary
from sqlalchemy import Date, DateTime, Time, Identity, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create Database engine
engine = create_engine('sqlite:///.sqlite', echo=True)

# Define the classes for the db tables
base = declarative_base()

class MediaType(base):
    __tablename__ = 'media_type'

    id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Media(base):
    __tablename__= 'media'
    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    title=Column(Text, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Creator(base):
    __tablename__ = 'creator'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    first_name=Column(Text, nullable=False)
    last_name=Column(Text, nullable=False)
    picture=Column(LargeBinary)

class Role(base):
    __tablename__ = 'role'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name=Column(Text, nullable=False)

class MediaCreator(base):
    __tablename__ = 'media_creator'

    media_id=Column(BigInteger, nullable=False, primary_key=True, ForeignKey='media.id')
    creator_id=Column(BigInteger, nullable=False, primary_key=True, ForeignKey='creator.id')
    creator_role_id=Column(BigInteger, nullable=False, ForeignKey='role.id')

class Publisher(base):
    __tablename__ = 'publisher'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name=Column(Text, nullable=False)

class MediaPublisher(base):
    __tablespace__ = 'content_publisher'

    media_id = Column(BigInteger, nullable=False, primary_key=True, ForeignKey='meida.id')
    publisher_id = Column(BigInteger, nullable=False, primary_key=True, ForeignKey='publisher.id')

class ContentType(base):
    __tablespace__='content_type'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = name=Column(Text, nullable=False)

class Media_ContentType(base):
    __tablespace__='media_contenttype'

    media_id = Column(BigInteger, nullable=False, primary_key=True, ForeignKey='meida.id')
    content_type_id = Column(BigInteger, nullable=False, primary_key=True, ForeignKey='content_type.id')

class ResourceLocation(base):
    __table_space__ = 'resource_location'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False)

