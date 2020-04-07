from Flask import Flask, render_template, request
from wtforms import Form, TextField, validators, SubmitField, IntegerField
import random
from surprise import dump, SVD
import pickle
from collections import defaultdict
import pandas as pd


# Create app
app = Flask(__name__)


class ReusableForm(Form):
    """User entry form for entering game rankings for recommendations"""

    Userdf = pd.DataFrame.from_csv('UserReviews.csv')
    Top30 = Userdf.Game_Title.value_counts().index[0:30]
    GamestobeRanked = random.sample(list(Top30), k=4)

    # Username
    username = TextField("Enter a username:", validators=[
                     validators.InputRequired()])
    print('\n Consider the following games: \n')
    print(GamestobeRanked[0]+'\n')
    print(GamestobeRanked[1]+'\n')
    print(GamestobeRanked[2]+'\n')
    print(GamestobeRanked[3]+'\n')
    print(' \nPlease rank your interest in these games from 1 to 4. 1 is the best, and 4 is the worst:\n')

    Rank1 = IntegerField(GamestobeRanked[0], default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])
    Rank2 = IntegerField(GamestobeRanked[1], default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])
    Rank3 = IntegerField(GamestobeRanked[2], default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])
    Rank4 = IntegerField(GamestobeRanked[3], default=0, validators=[validators.InputRequired(),
                                                 validators.NumberRange(min=1, max=4,
                                                 message='Ranking must be between 1 and 4')])

    # Submit button
    submit = SubmitField("Enter")


def load_surprise_model():
    """Load in the pre-trained model"""
    global model
    infile = open('predictions', 'rb')
    predictions = pickle.load(infile)
    infile.close()

def get_top_n(predictions, n=10):
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    return top_n

def recommend():
    algo = SVD()
    top_n = get_top_n(predictions, n=10)


# Home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # Create form
    form = ReusableForm(request.form)

    # On form entry and all conditions met
    if request.method == 'POST' and form.validate():
        # Extract information
        username = request.form['username']
        Rank1 = int(request.form['Rank1'])
        Rank2 = int(request.form['Rank2'])
        Rank3 = int(request.form['Rank3'])
        Rank4 = int(request.form['Rank4'])
    # Send template information to index.html
    return render_template('index.html', form=form)


if __name__ == "__main__":
    print(("* Loading SVD model and Flask starting server..."
           "please wait until server has fully started"))
    load_surprise_model()
    # Run app
    app.run(host="0.0.0.0", port=80)
