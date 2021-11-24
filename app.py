from flask import Flask, json ,request,jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')


@app.route('/character/',methods=["POST","GET"])
def getCharacters():
    
    lista=requests.get('https://er-public-resources.s3.amazonaws.com/characters.json')
    
    return jsonify(lista.json())


@app.route('/character/<int:id>')
def getCharacterId(id):
    lista=requests.get('https://chavo.s3.us-east-2.amazonaws.com/characters.json')
    
    
    for element in lista.json():
        if(id==element["id"]):
            return jsonify(element)
        else:
            jsonify({"message":"usuario no encontrado"})

if __name__ == '__main__':
    app.run(debug=True)