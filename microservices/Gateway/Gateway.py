import flask as fl
import requests

app = fl.Flask(__name__)


@app.route("/", methods=['GET'])
def index():
	return ""


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5004, debug=True)