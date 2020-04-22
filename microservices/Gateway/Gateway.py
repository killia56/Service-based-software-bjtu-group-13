import flask as fl
import requests

app = fl.Flask(__name__)


@app.route("/", methods=['GET'])
def index():
	return "G"


if __name__ == '__main__':
	# url = 'http://localhost:5001/login'
	# myobj = {'somekey': 'somevalue'}
	# print(requests.get(url, data = myobj))
	app.run(host='0.0.0.0', port=5004, debug=True)signin