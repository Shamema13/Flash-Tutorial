from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def home():
    users=["gokul","nava","shami","kiruba","nithya"]
    district="erode"
    message="hello"
    return render_template("home.html",users=users,place="sathy",zip=district ,msg=message,followers=0)

@app.route("/user/<user_name>")
def user(user_name):
    return render_template("user.html",user_name=user_name, followers=10)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/abc")
def sakthi():
    return "navasakthi"

@app.route("/welcome/<Name>")
def welcome(Name):
    return "welcome "+Name
    
if __name__=="__main__":
    app.run(debug=True)