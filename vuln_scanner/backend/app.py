from flask import Flask
from flask_cors import CORS

from routes.scan_routes import scan_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(scan_bp)

# Home route

@app.route("/")
def home():

    return {
        "message": "Linux Vulnerability Scanner Backend Running"
    }

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
