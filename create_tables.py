from xmlrpc.client import _datetime_type
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column

# Data Types to Import - Importing everything at first, clean up to keep
# Only the ones used.
from sqlalchemy import SmallInteger, Integer, BigInteger, Text, LargeBinary
from sqlalchemy import Date, DateTime, Time, JSON, Identity, Boolean, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

# Create Database engine
engine = create_engine('sqlite:///brainery.sqlite', echo=True)

# Define the classes for the db tables
Base = declarative_base()

class Media(Base):
    __tablename__= 'media'
    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    title=Column(Text, nullable=False)
    cover=Column(Text)
    year_published = Column(SmallInteger)
    date_acquired=Column(Date)

    def __init__(self, title, cover, year_published, date_acquired):
        self.id = id
        self.title= title
        self.cover = cover
        self.year_published = year_published
        self.date_acquired = date_acquired

class MediaType(Base):
    __tablename__ = 'media_type'

    id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Creator(Base):
    __tablename__ = 'creator'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    first_name=Column(Text, nullable=False)
    last_name=Column(Text, nullable=False)
    picture=Column(LargeBinary)

    def __init__(self, id, first_name, last_name, picture):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.picture = picture
        self.full_name = f"{last_name}, {first_name}"
        self.display_name = f"{first_name} {last_name}"

class Role(Base):
    __tablename__ = 'role'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name=Column(Text, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Publisher(Base):
    __tablename__ = 'publisher'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name=Column(Text, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Location(Base):
    __tablename__ = 'location'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Codec(Base):
    __tablename__ = 'codec'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False, unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Resolution(Base):
    __tablename__ = 'resolution'

    id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False, unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name
    

class Video(Base):
    __tablename__ = 'video'

    id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    media_id=Column(BigInteger, ForeignKey('media.id'))
    codec_id=Column(BigInteger, ForeignKey('codec.id'))
    is_hd = Column(Boolean, nullable=False)
    resolution_id =Column(BigInteger, ForeignKey('resolution.id'))
    length=Column(Time, nullable=False)

    def __init__(self, id, media_id, codec_id, is_hd, resolution_id, length):
        self.id = id
        self.media_id = media_id
        self.codec_id = codec_id
        self.is_hd = is_hd
        self.resolution = resolution_id
        self.length = length

class Website(Base):
    __tablename__ = 'website'

    id=Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False)
    url =  Column(Text)
    login = Column(Text, nullable=False)

    def __init__(self, id, name, url, login):
        self.id = id
        self.name = name
        self.url = url
        self.login = login

class Book(Base):
    __tablename__ = 'book'

    media_id = Column(BigInteger, ForeignKey('media.id'), nullable=False, primary_key=True)
    isbn = Column(Text, nullable=False, unique=True)
    pages = Column(Integer)

    def __init__(self, media_id, isbn, pages, cover):
        self.media_id = media_id
        self.isbn = isbn
        self.pages = pages
        self.cover = cover
        
class Category(Base):
    __tablename__ = 'category'

    id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False)
    parent_id = Column(BigInteger, ForeignKey('category.id'))

    def __init__(self, id, name, parent_id):
        self.id = id
        self.name = name
        self.parent_id = parent_id

class Format(Base):
    __tablename__ = 'format'

    id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    name = Column(Text, nullable=False, unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Filename(Base):

    __tablename__ = 'filename'

    id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
    media_id = Column(BigInteger, ForeignKey('media.id'), nullable=False)
    filename = Column(Text, nullable=False)

#  CrossReference Tables

class MediaXCreator(Base):
    __tablename__ = 'mediaXcreator'

    media_id=Column(BigInteger, ForeignKey('media.id'), nullable=False, primary_key=True)
    creator_id=Column(BigInteger, ForeignKey('creator.id'), nullable=False, primary_key=True)
    creator_role_id=Column(BigInteger, ForeignKey('role.id'), nullable=False)

    def __init__(self, media_id, creator_id, creator_role_id):
        self.media_id = media_id
        self.creator_id = creator_id
        self.role_id = creator_role_id

class MediaXPublisher(Base):
    __tablename__ = 'media__publisher'

    media_id = Column(BigInteger, ForeignKey('media.id'), nullable=False, primary_key=True)
    publisher_id = Column(BigInteger, ForeignKey('publisher.id'), nullable=False, primary_key=True)

    def __init__(self, media_id, publisher_id):
        self.media_id = media_id
        self.publisher_id = publisher_id

    
class VideoXResolution(Base):
    __tablename__ = 'videoXresolution'

    video_id = Column(BigInteger, ForeignKey('video.id'), primary_key=True)
    resolution_id = Column(BigInteger, resolution_id=('resolution.id'), primary_key=True)

    def __init__(self, video_id, resolution_id):
        self.video_id = video_id
        self.resolution_id = resolution_id

class MediaXWebsite(Base):
    __tablename__ = 'mediaXwebsite'

    media_id = Column(BigInteger, ForeignKey('media.id'), nullable=False, primary_key=True)
    website_id = Column(BigInteger, ForeignKey('website.id'), nullable=False, primary_key=True)

    def __init__(self, media_id, website_id):
        self.media_id = media_id
        self.website_id = website_id

class LocationXMedia(Base):
    __tablename__ = "mediaXlocation"

    media_id = Column(BigInteger, ForeignKey('media.id'), nullable=False, primary_key=True)
    location_id = Column(BigInteger, ForeignKey('location.id'), nullable=False, primary_key=True)

# Create the database
Base.metadata.create_all(engine)

### Insert Data ###

## Just playin' around to see how insertion works with sql alchemy
# create session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

resolutions = {1009: 'HD', 1010: 'SD'}

with session:
    for key_, val_ in resolutions.items():
        row = Resolution(id = key_, name=val_)
        session.add(row)
    session.commit()


# class FormatExtensions(Base):
#     __tablename__ = 'format_extension'

#     id = Column(BigInteger, Identity(start=1001, cycle=True), primary_key=True)
#     format_id = Column(BigInteger, ForeignKey=('format.id'), nullable=False)
#     extension = Column(Text, nullable=False)

#     def __init__(self, id, format_id, extension):
#         self.id = id
#         self.format_id = format_id
#         # Convert the extension to lowercase and remove whitespace 
#         # so that it is easier to  maintain unique extensions
#         self.extension = extension.lower()

#         # if present, Remove the first period from an extension
#         if extension[0] == '.':
#             extension = extension[1:0]

#         # Software will check for invalid characters in extensions,
#         # But check to make sure, just in case. Some of these are 
#         # allowed on some systems and not others. Best to avoid all
#         # of them.
#         # First, add the ascii control characters (0-31)
#         invalid_characters = [chr(x) for x in range(0, 32)]
#         # Merge with the rest of the list
#         invalid_characters = invalid_characters \
#                         +['/', '<', '>', ':', '"', "'", '\\', '|', '?', '*']

#         # Check if the extension contains any of the invalid characters and
#         # remove them
#         extension = ''.join([c for c in extension if c not in invalid_characters])