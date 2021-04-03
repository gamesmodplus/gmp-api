from flask import Blueprint

blueprint_page = Blueprint('blueprint_page', __name__)

@blueprint_page.route('/')
def index():
    return '<p>This is a blueprint page test</p>'
