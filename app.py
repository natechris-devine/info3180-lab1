"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from flask import Flask, render_template

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''

@app.route('/')
def home():
    return "My Home Page"

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    #  - not working on my machine atm: would need to configure network domain
    app.run(debug=True, host="0.0.0.0", port=8080)
    # app.run(debug=True, host="localhost", port=8080)
