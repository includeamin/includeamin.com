from flask import Blueprint

Projects = Blueprint('WBC', __name__, template_folder='templates')


@Projects.route('/projects/<name>')
def get_projects_info(name):
    return "{0}'s Info will ready ASAP".format(name)