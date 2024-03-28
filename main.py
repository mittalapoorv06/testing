from flask import Flask
from apis.users import users_api

app = Flask(__name__)

app.register_blueprint(users_api)

@app.route("/home", methods=['GET'])
def hello():
    return "Welcome to nillu"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(debug=True)