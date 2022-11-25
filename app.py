from flask import Flask,render_template
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLAlchemy_DATABASE_URL']= "sqlite:///Todo.db"
#app.config['SQLAlchemy_TRACK_MODIFICATION']= False



#db=SQLAlchemy(app)

@app.route("/<a>/<b>")
def sub(a,b):
    return str(int(a)-int(b))
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/surajit")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/superman")
def hello_world1():
    return "<p>Hello, Wolkjfgjkdhrld! superman</p>"
@app.route("/add/<a>/<b>")
def add(a,b):
    return str(int(a)+int(b))
@app.route("/mul/<a>/<b>")
def mul(a,b):
    return str(int(a)*int(b))
@app.route("/div/<a>/<b>")
def div(a,b):
    return str(int(a)/int(b))
#@app.route("/sub/<a>/<b>")
#def sub(a,b):
    #return str(int(a)-int(b))
@app.route("/suqare/<a>/<b>")
def square(a,b):
    return str(int(a)**int(b))
@app.route("/mod/<a>/<b>")
def mode(a,b):
    return str(int(a)%int(b))





if __name__ == "__main__":
    app.run()
    