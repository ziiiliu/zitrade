from api_consumer import OddsApiClient

from flask import Blueprint, current_app

blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    return "This is odds-api-gateway. Navigate to these endpoints: <TODO>"

@blueprint.route('/sports')
def get_all_sports():
    api_client: OddsApiClient = current_app.config["api_client"]
    res = api_client.get_all_sports()
    return res