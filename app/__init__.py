from flask_api import FlaskAPI
from instance.config import app_config
from flask import request, jsonify, abort

def create_app(config_name):
    from app.model import LoxAPI

    app = FlaskAPI(__name__,
                   instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/s3/thumbnails', methods=['GET'])
    def get_thumbnails():

    @app.route('/s3/save', methods=['POST'])
    def save_file():

    @app.route('/s3/delete', methods=['DELETE'])
    def delete_file():

    @app.route('/user/register', method=['POST'])
    def add_user():

    @app.route('/user/erase_user', method=['DELETE'])
    def erase_user():

    @app.route('/user/login', method=['POST'])
    def login():

    @app.route('/lox/interpret', method=['POST'])
    def compile():

