from flask import Flask
# Import flask

app = Flask(__name__)
# make the flask app

app.static_folder = 'static'
# defines static folder

@app.route("/")
#establishes first route
def index():
    return "Hello"
#makes the function for / route

if __name__ == "__main__":
    app.run(debug=True)
# runs the app