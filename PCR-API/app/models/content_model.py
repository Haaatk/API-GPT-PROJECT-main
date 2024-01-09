from . import db
from datetime import datetime

class Content(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Colum(db.String(100),nullable=False)
    url = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50))
    published_date = db.COlumn(db.DateTime, defaut=datetime.utcnow)
    summary = db.Column(db.Text)

    #Métriques intéressantes
    views = db.Column(db.Integer, default =0)
    likes = db.Column(db.Integer,defaut=0)

    def __repr__(self):
        return f'<Content {self.title}>'