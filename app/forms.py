from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class QueryCreateForm(FlaskForm):
    word = StringField('추가할 키워드', validators=[DataRequired(), Length(min=1, max=25)])
    nums = IntegerField('기사 수', validators=[DataRequired()])
    