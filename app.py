import os

from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restx import Api

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    version="0.1",
    title="Example API",
    description="Example API for an Example",
    validate=True,
)

app.register_blueprint(blueprint)

from api.apiOne.routes import api as nsOne

from api.apiTwo.routes import api as nsTwo

api.add_namespace(nsOne)
api.add_namespace(nsTwo)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8060)))
