from flask import Flask, redirect, url_for
from models import db
from catalog import bp as catalog_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-change-me'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecom.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(catalog_bp)

    @app.route('/')
    def index():
        return redirect(url_for('catalog.products'))

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
