# Tech Challenge 
## Pokemon Shakspearean Translator
A translator that allows users to search for a Pokemon character and see its desctiption in Shakspearean English.
The app was created with Python and Flask on Windows 10 in Visual Studio Code.

#### A live version of the app is available here: https://truelayer-challenge.herokuapp.com/

#### (See below for information on install requirements.)

## Local setup
If you need to create it locally, below are commands for Win/Unix systems.

1. Create a virtual enviroment folder
    #### macOS/Linux
    * sudo apt-get install python3-venv 
    * python3 -m venv env

    #### Windows
    * python -m venv env

2. Install Flask and install Requests
    #### macOS/Linux
    * pip3 install flask
    * pip3 install requests

    #### Windows
    * pip install flask
    * pip install requests

3. Run the app
    #### macOS/Linux
    * $ export FLASK_APP=app.py
    * $ flask run

    #### Windows
    * C:\path\to\app>set FLASK_APP=app.py
    * flask run
