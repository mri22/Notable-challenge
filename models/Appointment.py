class Appointment:

	def __init__(self, appointment_id, patient_first_name, patient_last_name, date, time, kind):

		self.appointment_id = appointment_id
		self.patient_first_name = patient_first_name
		self.patient_last_name = patient_last_name
		self.date = date
		self.time = time
		self.kind = kind

	def get_appointment_id(self):
		return self.appointment_id

	def get_patient_first_name(self):
		return self.patient_first_name

	def set_patient_first_name(self, patient_first_name):
		self.patient_first_name = patient_first_name

	def get_patient_last_name(self):
		return self.patient_last_name

	def set_patient_last_name(self, patient_last_name):
		self.patient_last_name = patient_last_name

	def get_date(self):
		return self.date

	def set_date(self, date):
		self.date = date

	def get_time(self):
		return self.time

	def set_time(self, time):
		self.time = time

	def get_kind(self):
		return self.kind

	def set_kind(self, kind):
		self.kind = kind