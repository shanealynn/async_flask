
# Async Flask Test

===========

Test of asynchronous flask communication with web page. 

This repository is a sample flask application that updates a webpage using a background thread for all users connected.
It is based on the very useful Flask-SocketIO code from Miguel Grinberg.

https://github.com/miguelgrinberg/Flask-SocketIO

To use - please clone the repository and then set up your virtual environment using the requirements.txt file with pip and virtualenv. You can achieve this with:


    git clone https://github.com/shanealynn/async_flask
    cd async_flask
    # Create a virtual environment
    python3.9 -m venv venv
    # Activate that virtual environment
    source venv/bin/activate
    # Install the project requirements.
    pip install -r requirements.txt  #(or in Windows - sometimes python -m pip install -r requirements.txt )


Start the application with:

<code>
python application.py
</code>

And visit http://localhost:5000 to see the updating numbers.

## ChangeLog

15-Jul-2014: Initial Version
19-May-2018: Update to Python3.3
10-Apr-2022: 
 - Update to Python3.9 
 - fixes for threading.isAlive() -> threading.is_alive()
 - Update socketIO version on Frontend
