from . import db
from datetime import datetime

class UserInteraction(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    content_id = db.Column(db.Integer,db.ForeignKey('content.id'),nullable=False)
    interaction_type = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<UserInteraction {self.interaction_type} by {self.user_id} on {self.content_id}>'