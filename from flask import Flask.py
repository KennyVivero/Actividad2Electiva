from flask import Flask
 
app = Flask(__name__)
 
@app.route('/Personas')
def home():
 
    personas = [
        {
            "nombre": "Maria",
            "edad": 26
        },
        {
            "nombre": "Brayan",
            "edad": 32
        },
        {
            "nombre": "Joel",
            "edad": 24
        },
        {
            "nombre": "Angelica",
            "edad": 30
        },
        {
            "nombre": "Manuel",
            "edad": 52
        }
       
    ]
 
    return personas
 
 
if __name__ == '__main__':
    app.run()
 