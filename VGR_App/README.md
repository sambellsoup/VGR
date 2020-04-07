# VG_Suggestor
Video Game Recommender

The goal of this project is to use user-rated data in order to create the basis for a video game recommendation system. 
The final application will be used to recommend entertainment to users based on input of preferred video games. 

This project will begin with game for the Nintendo Switch, but stretch goals involve extending
to other platforms including Mobile, PS4, etc. This project could even extend to other forms of media. 
If Johnny likes Zelda OoT and The Smurfs, maybe he would enjoy GhostBusters. 

The recommendation engine will be built with Single Value Decomposition (SVD) to estimate ratings 
based on the input ratings. The input ratings should be taken as rankings. For example, instead of giving individual games
a rating of 1-10, three games would be provided and the user would be instructed to put them in order of least enjoyable
to most enjoyable. The purpose of this is to create a more even distribution of ratings rather than
an inverse normal distribution where most ratings are either 10 or 1. 
A couple problems and decisions will need to be made regarding the scale of how many items to order, and how would
the user decide where to place an item if they are completely unfamiliar with it? 

How can you reasonably rank something you don't know anything about? 
This problem may be avoided by providing the user the option to cycle through available options. 
Once selected, the cycled options should be drawn from the popular/unpopular stacks alternately. 

The problem of scaling the ranking system is difficult. How many items should be presented to the user for ranking? 
Perhaps the user should be able to choose how many items to be ranked. It could range from 2-10. 
Of course, how would numerical ratings then be assigned to each rank? 
If ranking two items, would it be fair to assign the less favorable item a 1 and the more favorable item at 10? 

The purpose of the ranking system is to encourage a normal distribution in our data. 
It may be better to limit our users choices to only even options to look something like this:

2 items:                  5 - 6

4 items:              4 - 5 - 6 - 7

6 items:          3 - 4 - 5 - 6 - 7 - 8

8 items:      2 - 3 - 4 - 5 - 6 - 7 - 8 - 9

10 items: 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10

-----------------------------------------------------------------------------

Objective 1 : Gather all available data

Objective 2 : Create user input functions

Objective 3 : Store data on AWS

Objective 4 : Deploy App

Objective 5 : Create data pipeline

-----------------------------------------------------------------------------

From a pool of the most reviewed 30 games, the user is asked to rank the 10 games they like or are most interested in. 
The user is offered the option to skip (cycle to a new game), or drop (reduce the number of games to rank). 

The recommendation input will require 4 ranked games. 4 is chosen because it is easy to maintain in the short-term memory so users will not need to write anything down while ranking 4 games at once. The system will be updated to include up to 10 games to be ranked once a drag-and-drop mechanism is incorporated. Pictures and game summaries will also be scraped and included in future version of the Video Game Recommendaiton(VGR) engine. 

A NLP feature will be included where the top ranked game is matched with the most similar game description. Also included in a future version will be the predicted top-rating of a game by a production company that only has produced one game (an indie game). The closest matching indie game will also be included in the results. 

A feature to include cycling through games to be ranked, in the case the user has not played or has no idea about a game. 

Run and test different algorithms to find the best one.

https://towardsdatascience.com/building-and-testing-recommender-systems-with-surprise-step-by-step-d4ba702ef80b

Features to work on:
  Click and drag interface. Inspired by create your own tier list.
