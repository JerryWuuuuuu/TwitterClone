Routes
    - "/": This is just the splash page, and has buttons to point users to the sign up or login page
    - "/signup": This is the sign up page, users can sign up here 
    - "/login": This is the log in page, users can log in here 
    - "/home": Once a user is logged in, this is their home page, and displays all tweets in chronological order
    - "/tweet": This route is called when the user tweets, and just creates a new Tweet model 
    - "/profile/<author>": This route takes you to the profile page of the "author" of any tweet. If the "author" is the currently signed in user, they can logout. 
    - "/logout": This route is called when the user clicks the log out button, and just logs the user out
    - "/hashtag/<hashtag>": This is the hashtag page which displays all tweets that have the hashtag "hashtag" 
    - "/like/<id>": This route is called when someone likes or unlikes a tweet, and just increments or decrements the number of likes a tweet has 
    - "/delete/<id>": This route is called when a user deletes their tweet. Users can only delete their own tweets. 
    -"/hashtag": This page displays all current hashtags used sorted by the number of tweets that use it 
Design
    - I decided to have a nav bar for easy navigation between the home, profile, and hashtag page 
    - My colors, sign up and log in buttons match the ones twitter uses exactly which is pretty cool! 
    - I created the hashtag page for easy access to all the possible hashtag pages. Otherwise users wouldn't be able to go to specific hashtag pages without knowing the url. 
Run Server
    - To run the server, just run python manage.py runserver" 
