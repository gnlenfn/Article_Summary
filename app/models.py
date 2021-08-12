from sqlalchemy.orm import backref
from app import db

class Keywords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(15), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)

class Crawled_urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword_id = db.Column(db.Integer, db.ForeignKey('keywords.id', ondelete="CASCADE"))
    keyword = db.relationship('Keywords', backref=db.backref("crawling", cascade='all, delete-orphan'))
    title = db.Column(db.String(100), nullable=False)
    word = db.Column(db.String(15))
    url = db.Column(db.String(200), nullable=False)
    summary = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)

