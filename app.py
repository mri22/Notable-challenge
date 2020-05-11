import flask
import json
from controller.Controller import Controller

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/doctors")
def getPhysicians():

	return json.dumps(controller.getDocs())

@app.route("/appointments")
def getAppointments():
	doc_id = flask.request.args.get('doctorID')
	date = flask.request.args.get('date')

	return json.dumps(controller.getDocApps(int(doc_id), date))

@app.route("/deleteAppointment", methods=['DELETE'])
def deleteAppointment():
	doc_id = flask.request.args.get('doctorID')
	app_id = flask.request.args.get('appointmentID')

	return controller.deleteDocAppointment(int(doc_id), int(app_id))

@app.route("/addAppointment", methods=['POST'])
def addAppointment():
	doc_id = int(flask.request.args.get('doctorID'))
	f_name = flask.request.args.get('fName')
	l_name = flask.request.args.get('lName')
	date = flask.request.args.get('date')
	time = flask.request.args.get('time')
	kind = flask.request.args.get('kind')

	return json.dumps(controller.addAppointment(doc_id, f_name, l_name, date, time, kind))

if __name__ == '__main__':
	controller = Controller()
	app.run(host='0.0.0.0', debug=True)
