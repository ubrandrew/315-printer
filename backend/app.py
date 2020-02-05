from flask import Flask, escape, request, make_response, jsonify, abort
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
import os
import json
import pathlib
import jwt
import datetime
from werkzeug.utils import secure_filename
from config import KEY


PASS = KEY
SECRET = os.environ.get('JWT_SECRET')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'temp_doc_store')

app = Flask(__name__)
cors = CORS(app, resources={
    r"*": {
        "origins": "*"
    }
})

bcrypt = Bcrypt(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=30)

@app.route('/print', methods=['GET','POST'])
def print():
    if request.method == 'POST':
        input_file = request.files['file']
        filename = secure_filename(input_file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        input_file.save(path)
        os.system(f'lp -dHP_LaserJet_1018 {path}')
    return "ok"

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.json)
    if request.method == 'POST':
        if bcrypt.check_password_hash(PASS, request.json['creds']):
            response = {}
            token = encode_auth_token().decode('utf-8')
            response['token'] = json.dumps(token)
            return response
        else:
            return abort(404)
    else:
        return


def encode_auth_token():
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

if __name__ == "__main__":
    app.run(debug=True, )