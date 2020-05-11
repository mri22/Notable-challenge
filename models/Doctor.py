class Doctor:

	def __init__(self, doctor_id, first_name, last_name):
		# type: (int, str, str)

		self.doctor_id = doctor_id
		self.first_name = first_name
		self.last_name = last_name

	def get_doctor_id(self):
		return self.doctor_id

	def get_first_name(self):
		return self.first_name

	def set_first_name(self, first_name):
		self.first_name = first_name

	def get_last_name(self):
		return self.last_name

	def set_last_name(self, last_name):
		self.last_name = last_name