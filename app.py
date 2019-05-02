from flask import Flask,send_from_directory
from Menu.WBC.app import WBC
app = Flask(__name__)
app.register_blueprint(WBC)

@app.route("/")
def index():
    return send_from_directory('./Static/',filename='index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)