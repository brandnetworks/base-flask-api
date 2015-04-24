from flask import Blueprint, jsonify
from .model import Health

blueprint = Blueprint('health', __name__)


@blueprint.route('/', methods=['GET'])
def __get_health__():
    health = Health()
    return jsonify(health.get_data())
