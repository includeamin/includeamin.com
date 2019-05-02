from flask import Blueprint

WBC = Blueprint('WBC', __name__, template_folder='templates')

@WBC.route("/demo")
def demo():
    return "<p>Coming soon</p>"
