from . import db
from werkzeug.security import generate_password_hash , check_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime)

    #Info de profilage avancé
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    location = db.Column(db.String(100))
    occupation = db.Column(db.string(100))
    
    #Champ pour pref de l'utilisateur
    interests = db.relationship('Interesst',backref='user',lazy='dynamic')
    interactions = db.relationship('UserInteraction', backref='user',lazy='dynamic')

    #Méthode pour la sécurité
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}'    
