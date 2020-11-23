## Icebreaker - Thunkable WebAPI block example 

This project serves as a simple API serving two GET enabled enpoints, **count** and **question**.

The **count** endpoint doesn't require a parameter, and returns the overall count of items that your Thunkable UI can randomly select from.

The **question** endpoint requires the parameter item (e.g. URL/question?item=9) where the item parameter is the randomly selected value from 0 to count - 1.

Note that Thunkable will not recognize LOCALHOST as a webserver, so you will need to serve this on Heroku, Google Cloud or similar, or alternatively (and temporarily) using NGROK.

You do not need to set any header parameters within your Thunkable WebAPI block; simply set your Thunkable WebAPI URL with the appropriate (i.e. count vs. question) endpoint.  When calling the question endpoint, create an object with fields **item** set to your UI's randomly obtained value, and then use and set a Thunkable WebAPI query parameter block to this object.
