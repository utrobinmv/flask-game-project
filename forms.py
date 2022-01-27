from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange

class StartForm(FlaskForm):
    size = RadioField(
        "Поле",
        coerce=str,
        choices=[
            ("7x7"),
            ("8x8"),
            ("9x9"),
        ],
    )
    
    submit = SubmitField("Начать игру")

class GameForm(FlaskForm):
    way = SelectField(
        "Укажи направление в которое желаете отправится",
        coerce=int,
        choices=[
            (0, "Вверх"),
            (1, "Вниз"),
            (2, "Влево"),
            (3, "Вправо"),
        ],
    )
    number_steps = IntegerField(
        "Как далеко планируете продвигаться?",
        validators=[DataRequired(), NumberRange(min=1)],
        default=1,
    )
    submit = SubmitField("Идем")
