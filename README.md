## Icebreaker - Thunkable WebAPI block example 

This project serves as a simple API serving two GET enabled endpoints, **count** and **question**.

Two files within the assets folder NAMES and QUESTIONS contain a list of names and icebreaker questions, respectively.  The NAMES file additionally contains HTML color codes for the foreground and background of the displayed text.

The **count** endpoint doesn't require a parameter, and returns the overall count of items that your Thunkable UI can randomly select from, which is simply the count of the rows within the NAMES file times the count of the rows within the QUESTIONS file.

The **question** endpoint requires the parameter item (e.g. URL/question?item=9) where the item parameter is the randomly selected value from 0 to count - 1.  The question end point returns a JSON object similar to this:

`{"name": "George", "question": "Favorite Food?", "fg": "#000000", "bg": "#FFFF00"}`

Note that Thunkable will not recognize LOCALHOST as a webserver, so you will need to serve Flask app on Heroku, Google Cloud or similar, or alternatively (and temporarily) using NGROK.

You do not need to set any header parameters within your Thunkable WebAPI block; simply set your Thunkable WebAPI URL with the appropriate (i.e. count vs. question) endpoint.  When calling the question endpoint, create an object with fields **item** set to your UI's randomly obtained value, and then use and set a Thunkable WebAPI query parameter block to this object.

## Example Usage

Here's a link to the icebreaker Thunkable project:
https://x.thunkable.com/copy/b6b392fdd114c72753d38831a2ea8bf6  Note: this link may expire.  Please message me if you need to obtain a new project link, or try to search for the Icebreaker public project within Thunkable.

Note the URL variable within the scnHome's blocks.  

Assuming you have localhost enabled on your machine, run app.py from this project which will host the API at http://127.0.0.1:8080.  You can test your hosting by pointing your browser to the count endpoint; i.e. http://127.0.0.1/count which should return an integer value.  You can test the question endpoint by pointing your browser to http://127.0.0.1/question?item=1.

Install NGROK, then start NGROK as follows:  `>ngrok http 8080 `  This will route your localhost's http traffic from port 8080 to a URL that NGROK will display.  Cut and paste that URL and replace the Thunkable scnHome URL block's variable's value with the this url (http) displayed on the NGROK output.

Now you can open Thunkable Live on your mobile device and "Live Test" within Thunkable.  Press the dice to display a new icebreaker screen, depicting a name and icebreaker question.   Change the assets/names.csv and assets/questions.csv files as you require, restarting the webserver after you make these changes.

If you'd like to explore hosting your endpoint on a cloud service, please refer to the document [AWSENDPOINT.md](AWSENDPOINT.md) included within this repo.
