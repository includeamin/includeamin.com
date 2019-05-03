from flask import Blueprint
import requests
import json


MainPage = Blueprint('MainPage', __name__, template_folder='templates')

@MainPage.route('/mainpage/info/services/usercount')
def get_services_users_count():
    try:
        data = requests.get("http://89.32.251.131:3022/includeamin/users/count").content
        data = json.loads(data)["State"]
        if data == True:
            return data["Description"]
        return 'FAILD TO CONNECTION '
    except Exception as ex:
        return ex.args
