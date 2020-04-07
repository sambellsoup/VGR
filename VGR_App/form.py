from wtforms import (Form, TextField, validators, SubmitField, IntegerField)
import random

class ReusableForm(Form):
    """User entry form for entering game rankings for recommendations"""

    Userdf = pd.DataFrame.from_csv('UserReviews.csv')
    Top30 = Userdf.Game_Title.value_counts().index[0:30]
    GamestobeRanked = random.sample(list(Top30), k=4)

    # Username
    username = TextField("Enter a username:", validators=[
                     validators.InputRequired()])
    print('\n Consider the following games: \n' + GamestobeRanked + ' \nPlease rank your interest in these games from 1 to 4. 1 is the best, and 4 is the worst:\n')
    Rank1 = IntegerField(GamestobeRanked[0])
                         default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])
    Rank2 = IntegerField(GamestobeRanked[1])
                         default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])
    Rank3 = IntegerField(GamestobeRanked[2])
                         default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])
    Rank4 = IntegerField(GamestobeRanked[3])
                         default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])

    # Submit button
    submit = SubmitField("Enter")
