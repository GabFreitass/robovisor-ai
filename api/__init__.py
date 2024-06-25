from flask import Blueprint, Flask
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from api.config import Config
from api.auth.routes import auth
from api.transcribe.routes import transcribe
from openai import OpenAI

app = Flask(__name__)
app.config.from_object(Config)
api = Blueprint("api", __name__, url_prefix="/api")

login_manager = LoginManager()
login_manager.init_app(app)

jwt_manager = JWTManager(app)
cors = CORS(app)
openai = OpenAI(api_key=Config.OPENAI_KEY)

# Blueprint registers
api.register_blueprint(auth)
api.register_blueprint(transcribe)


app.register_blueprint(api)
