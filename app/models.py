
#from flask import url_for
from app import db

class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))

class List(db.Model):
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_title = db.Column(db.String, index=True)
    appointment_date = db.Column(db.String)
    starting_time = db.Column(db.String)
    duration = db.Column(db.String)
    appointment_location = db.Column(db.String)
    customer_name = db.Column(db.String)
    notes = db.Column(db.String)
    appointment_status = db.Column(db.String)

