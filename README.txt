Welcome to our SI 206 Final Project!

Team Name: Team Python
Members: Andrew DeLave, Matthew Steinberg

Description:
This program takes personalized information from Spotify's and Gmail's APIs to deliver data visualizations.


Instructions for use:
1. Open Terminal or Command Line.
	- Install required packages (others are most likely already installed)
		- pip install spotipy
		- pip install seaborn
		
		- pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
		


2. Things to note:
	- These visualizations use personalized data from Spotify and Gmail.
		- Our profile information has been stored in cache files for easy running of the program.
		- Delete .cache-andrewdelave, .DS_Store, and token.pickle if you would like to use your own profiles.
	
	- The .csv files hold the outputted data manipulations.

	- Authorization keys and access tokens are stored in credentials.json and spotify_info.py

	- There are three visualizations in total.
		- The second Spotify visualization will not run until the first is closed
			- This visualization is the bonus



3. Run programs in this order:
	- spotify.py
		- This program will redirect the user to a localhost address in their web browser.
		- Paste the entire url it directed you to into the command line as instructed.
	- spotify_manipulations.py
	- spotify_visualizations.py
		- Exit the first visualization to see the second
	- gmail.py
	- gmail_manipulation.py
	- gmail_visualization.py


