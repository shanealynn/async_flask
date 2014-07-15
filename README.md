async_flask

Shane Lynn 15/07/2014

===========

Test of asynchronous flask communication with web page. 

This repository is a sample flask application that updates a webpage using a background thread for all users connected.
It is based on the very useful Flask-SocketIO code from Miguel Grinberg.

https://github.com/miguelgrinberg/Flask-SocketIO

To use - please clone the repository and then set up your virtual environment using the requirements.txt file with pip and virtualenv. You can achieve this with:

<code>
git clone https://github.com/shanealynn/async_flask
cd async_flask
virtualenv flaskiotest
./flaskiotest/Scripts/activate
pip install -r requirements.txt  #(or in Windows - sometimes python -m pip install -r requirements.txt )
</code>


Start the application with:

<code>
python application.py
</code>

And visit http://localhost:5000 to see the updating numbers.
