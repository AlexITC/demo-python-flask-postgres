import os

from flask import Flask, jsonify
from flask.cli import load_dotenv

from db import db
from routes import users, tasks

load_dotenv()

app = Flask(__name__)
database_host = os.getenv('POSTGRES_HOST')
database_name = os.getenv('POSTGRES_DATABASE')
database_username = os.getenv('POSTGRES_USERNAME')
database_password = os.getenv('POSTGRES_PASSWORD')
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql://{database_username}:{database_password}@{database_host}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(users.page, url_prefix='/users')
app.register_blueprint(tasks.page, url_prefix='/tasks')


@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not found'}), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run()
