from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    type = SelectField('type', validators=[DataRequired()],
                       choices = [('income','income',),
                                  ('expense','expense')
                                 ])
    
    category = SelectField('category', validators=[DataRequired()],
                       choices = [('rent','rent',),
                                  ('salary','salary'),
                                  ('investment','investment'),
                                  ('other','other')
                                 ])
    
    amount = IntegerField('Amount', validators=[DataRequired()])

    submit = SubmitField('Generate report')
                