from flask_sqlalchemy import SQLAlchemy

#Initalise l'extension SQLALchemy
db = SQLAlchemy()

#Import les modèles 
from .user_model import User
from .content_model import Content
from .user_interaction_model import UserInteraction
from .interest_model import Interest
