from flask import Flask
from flask import request
from generate import generatePlaylist
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/generate', methods=['POST'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def generate():
    data = request.get_json()
    return generatePlaylist(data)


if __name__ == '__main__':
    app.run(debug=True,  port=8080)
