# Needs to be in same folder as main App Python file
from <APP NAME> import db

class <FIRSTCLASS>(db.Model):
	__tablename__ = "<DISPLAY TABLE NAME"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String(80), nullable=False)

	def __init__(self, title, description):
		self.title = title
		self.description = description

	def __repr__(self):
		return '<title {}'.format(self.title)
