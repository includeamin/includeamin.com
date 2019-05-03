from flask import Blueprint

ServiceStatus = Blueprint('ServiceStatus',__name__,template_folder='static')

@ServiceStatus.route('/Services/Status/<name>')
def get_service_status(name):
    try:
        pass
    except Exception as ex:
        return '{0}'.format(ex.args)

