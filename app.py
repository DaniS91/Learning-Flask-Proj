from flask import Flask, render_template
# Import flask
# render_template function looks at the templates folder for templates, defined in route function

app = Flask(__name__)
# make the flask app

app.static_folder = 'static'
# defines static folder

@app.route("/")
#establishes first route
def index():
    return render_template('index.html')
#makes the function for / route

@app.route("/")
def about():
    return render_template('about.html')
#makes the function for about route

if __name__ == "__main__":
    app.run(debug=True)
# runs the app