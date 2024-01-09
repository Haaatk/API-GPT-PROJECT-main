from app import create_app

#Crée l'instance de l'app Flask

app = create_app()

#Start l'application 
if __name__ == "__main__":
    app.run(debug=True)