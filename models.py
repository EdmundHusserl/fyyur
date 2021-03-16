from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app) 


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15))
    image_link = db.Column(db.String(250))
    facebook_link = db.Column(db.String(250))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(100)) 
    genres = db.Column(postgresql.ARRAY(db.String, dimensions=1))
    
    def __repr__(self):
        return f"<Venue id={self.id}  name={self.name}>"
    

artist_shows = db.Table("artist_shows", 
                        db.Column("show_id", db.ForeignKey("show.id"), primary_key=True),
                        db.Column("artist_id", db.ForeignKey("artist.id"), primary_key=True))

venue_shows = db.Table("venue_shows",
                       db.Column("show_id", db.ForeignKey("show.id"), primary_key=True),
                       db.Column("venue_id", db.ForeignKey("venue.id"), primary_key=True))


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    phone = db.Column(db.String(15))
    image_link = db.Column(db.String(250))
    facebook_link = db.Column(db.String(250))
    seeking_venue = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(100))
    genres = db.Column(postgresql.ARRAY(db.String, dimensions=1))

    def __repr__(self):
        return f"<Artist id={self.id}  name={self.name}>"


class Show(db.Model):
    __tablename__ = "show"

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime(), nullable=False)
    artist_id = relationship("Artist", 
                             secondary=artist_shows, 
                             backref=db.backref("shows", lazy=True),
                             cascade="all, delete")
    
    venue_id = relationship("Venue",
                            secondary=venue_shows,
                            backref=db.backref("shows", lazy=True),
                            cascade="all, delete")

    def __repr__(self):
        return f"<Show id={self.id}  start_time={self.start_time}>"
