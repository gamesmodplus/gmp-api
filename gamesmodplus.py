from flask import Flask
from blueprint_page import blueprint_page
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(blueprint_page, url_prefix='/blueprint_page')

# A welcome message to test our server
@app.route('/')
def home():
    return "<h1>Welcome to gamesmodplus api</h1><p>Access the CORS proxy api by going to gmpcorsbypasser.herokuapp.com</p>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
