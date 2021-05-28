# Django-Basketball-Stats

The correct repository is "backing up"
The wrong repository is "Django-Basketball-Stats"

For my extra 30% I did the following:

1. I spend a lot of time setting up base.html which allowed me to use template extensions. Initially, base.html was 
extended to login.html, register.html, points.html, rebounds.html and index.html. However, I got rid off points.html
and rebounds.html for concision and base.html cannot extend register.html because it was messing with the login/logout
function (so i just manually added the styling for register.html.) As of now, base.html extends to login.html and index.html!

(The benefits of using template extensions allowed me to have a consistent look that was well styled in one template and could be used for most of the website!)

2. I also allowed a user to register through a form. For simplicity I created a new folder known as "register" 
that would handle the registration function. I was able to set up register.html which is a form that allows users
to register. When a user is not logged in/registered, they can only see the home page and the registration site
(base.html and register.html), however, after a user logins or registers, they have complete access to the whole website!


3. Lastly, I worked on the function of index.hmtl which allowed the user to choose from a variety of 15 players
and displayed that player's stats (in the form of points per game, rebounds per game, 2 pt%, 3 pt%, and games played). 
To do this, I used basketball-reference.com and exported the data as a CSV. I put all this data into "data.txt" and then used 
code in my view to read in this file. From there, I set the points, rebounds, etc. This allowed me to create NBAPlayer objects by 
looping through the players. So, I created the 15 players with the appropriate stats. (I had NBAPlayer, NBAPlayer2, and NBATeam.
The reason I needed NBAPlayer2 was to add some stats that I wanted but could not add to NBAPlayer because the models.py would
not let me edit the NBAPlayer model.) Finally, when the user clicks on a player, I check to see which is the "selected player" and
then displayed the appropriate statistics!

My last commit is 6d53dad772dbcecd0beb780e7c8d7c16332d4113
