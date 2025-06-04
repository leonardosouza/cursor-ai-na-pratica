from flask import Flask
from flask_cors import CORS
from src.calculator.api import calculator_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(calculator_bp)

if __name__ == '__main__':
    # Rodar em debug mode para desenvolvimento
    app.run(debug=True) 