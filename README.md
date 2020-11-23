## Icebreaker - Thunkable WebAPI block example 

This project serves as a simple API serving two GET enabled endpoints, **count** and **question**.

Two files within the assets folder NAMES and QUESTIONS contain a list of names and icebreaker questions, respectively.  The NAMES file additionally contains a HTML color codes for the foreground and background of the displayed text.

The **count** endpoint doesn't require a parameter, and returns the overall count of items that your Thunkable UI can randomly select from.

The **question** endpoint requires the parameter item (e.g. URL/question?item=9) where the item parameter is the randomly selected value from 0 to count - 1.  The question end point returns a JSON object similar to this:

`{"name": "George", "question": "Favorite Food?", "fg": "#000000", "bg": "#FFFF00"}`

Note that Thunkable will not recognize LOCALHOST as a webserver, so you will need to serve Flask app on Heroku, Google Cloud or similar, or alternatively (and temporarily) using NGROK.

You do not need to set any header parameters within your Thunkable WebAPI block; simply set your Thunkable WebAPI URL with the appropriate (i.e. count vs. question) endpoint.  When calling the question endpoint, create an object with fields **item** set to your UI's randomly obtained value, and then use and set a Thunkable WebAPI query parameter block to this object.
