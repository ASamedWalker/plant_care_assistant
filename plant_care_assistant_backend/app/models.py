from app import db

class User(db.Model):
  # User model fields
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  # Add other user fields like password, email, etc.

class Plant(db.Model):
  # Plant model fields
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), index=True)
  # care_instructions = db.Column(db.Text)
  # Add other plant fields like image, etc.
  # description, watering frequency, light requirements, temperature_range
  # humidity_level, date_planted, last_watered, is_favorite


class CareSchedule(db.Model):
  # CareSchedule model fields
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))
  plant = db.relationship('Plant', backref=db.backref('care_schedules', lazy=True))
  # Add other care schedule fields like frequency, etc.
  # care_date, task, notes, is_completed

class Post(db.Model):
  # Post model fields
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  content = db.Column(db.Text)
  # Add other post fields like image, etc.