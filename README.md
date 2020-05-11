# Notable-challenge
# Setup
1- install python 2

2- install `flaskl` framework:

`pip install Flask`

3- install `curl`:

`sudo apt install curl`

# Run
`python app.py`

# Test

Test GET requests using browser

- Get a list of all doctors ~ 

`http://0.0.0.0:5000/doctors`

- Get a list of all appointments for a particular doctor and particular day

`http://0.0.0.0:5000/appointments?doctorID=2&date=11/07/2020`

Test POST and DELETE using `curl`

- Delete an existing appointment from a doctor's calendar -> return appointment id

`curl -X DELETE 'http://0.0.0.0:5000/deleteAppointment?doctorID=2&appointmentID=105'`

- Add a new appointment to a doctor's calendar -> return new appointment added

`curl -X POST 'http://0.0.0.0:5000/addAppointment?doctorID=3&fName=Mark&lName=Daniels&date=11/07/2020&time=23:45&kind=follow_up'`
