from application import db
from datetime import datetime

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, default='income', nullable=False)
    category = db.Column(db.String(30), nullable=False, default='rent')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Income(id={self.id}, type={self.type}, category={self.category}, " \
               f"date={self.date}, amount={self.amount})"
