# Tech Challenge 
## Pokemon Shakspearean Translator
A translator that allows users to search for a Pokemon character and see its desctiption in Shakspearean English.
The app was created with Python and Flask on Windows 10 in Visual Studio Code.

#### A live version of the app is available here: https://truelayer-challenge.herokuapp.com/

#### (See below for information on install requirements.)


#### Part 1 (Answer)

Hi Rory,

The /token endpoint cannot be implemented asynchronously as only one concurrent request per access token is allowed. If a concurrent request is made, a ‘409 request_conflict’ error is returned. This is beyond the control of True Layer but it can be mitigated by using the Data API asynchronously.
The Data API supports asynchronous requests on all endpoints such as calls to list Accounts.
For more information on how to perform async requests, refer to the Data API documentation >  Data Guides >  Async Requests.

Hope this helps clarify things. Let me know if you need any more information.

Neil

======================================================================================



If you need to create it locally, below are commands for Win/Unix systems.

1. To create a virtual enviroment folder
    #### macOS/Linux
    sudo apt-get install python3-venv 
    python3 -m venv env

    #### Windows
    python -m venv env

2. Install Flask and requests
    #### macOS/Linux
    pip3 install flask
    pip3 install requests

    #### Windows
    pip install flask
    pip install requests

3. Run the app
    #### macOS/Linux
    $ export FLASK_APP=app.py
    $ flask run

    #### Windows
    C:\path\to\app>set FLASK_APP=app.py
    flask run
