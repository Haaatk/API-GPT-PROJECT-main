from flask import Flask
from flask_sqlalchemy import SQLALchemy

#Initialiser les extensions ici
db = SQLALchemy()
def create_app():
    ''' permet d'initialiser l'API'''
    app = Flask(__name__)

    #Configuration de l'application

    #Config de base
    app.config['SECRET_KEY'] = 'votre_clé_secrète_ici'

    #Config de la bdd
    app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///your-database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #Initaliser les extensions avec l'application 
    db.init_app(app)

    #Importe tous nos modules
    from .models import user_model, content_model
    from .services import recommendation_service
    from .routes import content_routes

    # Enregistrement des Blueprints des routes 
    app.register_blueprint(content_routes.bp)

    return app