from flask import Blueprint
import requests
import json
import logging

MainPage = Blueprint('MainPage', __name__, template_folder='templates')

@MainPage.route('/mainpage/info/services/usercount')
def get_services_users_count():
    try:
        data = requests.get("http://89.32.251.131:3022/includeamin/users/count").content
        data = json.loads(data)
        return str(data["Description"]["Count"])
    except Exception as ex:
        logging.warning(ex.args)
        return 'ERROR'
