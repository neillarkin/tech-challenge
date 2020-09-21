This is a translator that allows users to search for a Pokemon character and see its desctiption in Shakspearean English.

The app was created with Python and Flask on Windows 10 in Visual Studio Code.

A working version of the app is available here https://truelayer-challenge.herokuapp.com/ but if you need to create it locally, below are commands for Win/Unix systems.


1. To create a virtual enviroment folder
    # macOS/Linux
    sudo apt-get install python3-venv    # If needed
    python3 -m venv env

    # Windows
    python -m venv env

2. Install Flask and requests
    # macOS/Linux
    pip3 install flask
    pip3 install requests

    # Windows
    pip install flask
    pip install requests

3. Run the app
    # macOS/Linux
    $ export FLASK_APP=app.py
    $ flask run

    # Windows
    C:\path\to\app>set FLASK_APP=app.py
    flask run