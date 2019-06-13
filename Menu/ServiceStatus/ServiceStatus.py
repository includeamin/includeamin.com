from flask import Blueprint
import requests
from flask import send_from_directory
import logging
import sys,os

cwd = os.getcwd()

ServiceStatus = Blueprint('ServiceStatus', __name__, template_folder='templates')


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

                        'chichi_micro': 'https://chichiapp.ir:3000/',
                        "mads_micro":'https://chichiapp.ir:3030/',
                        'mads_auth':"https://chichiapp.ir:3031/",
                        'mads_user':"http://chichiapp.ir:3032",
                        'mads_res':"http://chichiapp.ir:3033",
                        'mads_game':"http://chichiapp.ir:3034"

                        }

        requests.get(service_list[name], timeout=1, verify=False)
        logging.warning('ture')
        return "true"
    except:
        logging.warning('false')
        return "false"


@ServiceStatus.route('/Service/status/availability')
def get_service_status_page():
    try:
        cwd = os.getcwd()
        return send_from_directory("./Static/",filename='ServiceStatus.html')
    except Exception as ex:
         return "Error"
