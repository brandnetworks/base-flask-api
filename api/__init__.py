import os
import re
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    docker_host = re.match('tcp://(.*):', os.getenv('DOCKER_HOST', ''))
    docker_ip = docker_host.group(1) if docker_host else ''

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URI',
        'postgres://base_api:pwgen_-sny_40@' + docker_ip + ':5432/postgres'
    )

    @app.route('/', methods=['GET'])
    def index():
        return jsonify(status='ok')

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(error='not found'), 404

    from health.controller import blueprint as health_module
    app.register_blueprint(health_module, url_prefix='/health')

    db.init_app(app)

    return app
