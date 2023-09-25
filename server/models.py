from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
import pytz

db = SQLAlchemy()

class Newsletter(db.Model, SerializerMixin):
    __tablename__ = 'newsletters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    published_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Africa/Nairobi')))
    edited_at = db.Column(db.DateTime, onupdate=datetime.now(pytz.timezone('Africa/Nairobi')))

    def __repr__(self):
        return f'<Newsletter {self.title}, published at {self.published_at}.>'
