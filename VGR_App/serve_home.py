from collections import defaultdict
from surprise import SVD, dump
import os
import pickle

Games = form.GamestobeRanked[0:4]
Rankings = [form.Rank1, form.Rank2, form.Rank3, form.Rank4]

def _replaceitem(x):
    if x == 1:
        return 7
    elif x == 2:
        return 6
    elif x == 3:
        return 5
    else:
        return x

Rankings = map(_replaceitem, Rankings)

for Game in Games:
    UserID.append(username)
Game_Title.extend(Games)
Rating.extend(Rankings)

UserRatings = pd.DataFrame([UserID, Game_Title, Rating]).transpose()
UserRatings.columns = ['UserID', 'Game_Title', 'Rating']

Userdf = Userdf.append(UserRatings, ignore_index=True)

infile = open('predictions','rb')
new_dict = pickle.load(infile)
infile.close()

print('According to your rankings, these are your recommended games:')
print("1. " + top_n.get(username)[0][0])
print("2. " + top_n.get(username)[1][0])
print("3. " + top_n.get(username)[2][0])
print("4. " + top_n.get(username)[3][0])
print("5. " + top_n.get(username)[4][0])
print("6. " + top_n.get(username)[5][0])
print("7. " + top_n.get(username)[6][0])
print("8. " + top_n.get(username)[7][0])
print("9. " + top_n.get(username)[8][0])
print("10. " + top_n.get(username)[9][0])
