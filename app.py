from flask import Flask, send_from_directory
from Menu.WBC.app import WBC
from Menu.Projects.information.projects import Projects
from Menu.MainPage.MainPage import MainPage
from Menu.ServiceStatus.ServiceStatus import ServiceStatus
from Menu.Keyvan.KBooks import keyvan
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(WBC)
app.register_blueprint(Projects)
app.register_blueprint(MainPage)
app.register_blueprint(ServiceStatus)
app.register_blueprint(keyvan)


@app.route("/")
def index():
    return send_from_directory('./Static/', filename='new_index.html')


@app.route("/<file_name>")
def get_files(file_name):
    return send_from_directory('./Static/', filename=file_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
