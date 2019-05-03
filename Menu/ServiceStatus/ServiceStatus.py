from flask import Blueprint
import requests
from flask import send_from_directory
import logging

ServiceStatus = Blueprint('ServiceStatus', __name__, template_folder='static')


@ServiceStatus.route('/Services/Status/<name>')
def get_service_status(name):
    try:
        service_list = {"animup_micro": "http://89.32.251.131:3000/",
                        "animup_auth": "http://89.32.251.131:3001/",
                        'animup_user': 'http://89.32.251.131:3002/',
                        'animup_accounting': 'http://89.32.251.131:3005/',
                        'animup_animation': 'http://89.32.251.131:3003/',
                        'animup_registery': 'http://89.32.251.131:5000/',
                        'animup_upload': 'http://89.32.251.131:3004/',

                        "words_micro": "http://89.32.251.131:3020/",
                        "word_auth": "http://89.32.251.131:3021/",
                        'word_user': 'http://89.32.251.131:3022/',
                        'words_accounting': 'http://89.32.251.131:3025/',
                        'word_game': 'http://89.32.251.131:3024/',
                        'words_registery': 'http://89.32.251.131:5000/',
                        'words_resource': 'http://89.32.251.131:3023/',

                        'chichi_micro': 'https://chichiapp.ir:3000/'

                        }

        requests.get(service_list[name], timeout=0.8, verify=False)
        logging.warning('ture')
        return "true"
    except:
        logging.warning('false')
        return "false"


@ServiceStatus.route('/Service/status')
def get_service_status_page():
    return send_from_directory("./static",filename='ServiceStatus.html')