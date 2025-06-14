import random
from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

savemessage = {}

@app.route('/thanks',methods=["POST"])
def thanks():
    if request.method=="POST":
        ID = random.randint(1000, 9999)
        sm = request.form.get("secreatmessge")
        savemessage[ID]=sm
        print(sm)
        return render_template('thanks.html',id=ID)


@app.route("/msge",methods=["POST"])
def msge():
    if request.method=="POST":
        try:
            IDs = int(request.form.get("ID"))
        except ValueError:
            return "<h2 style='color:red;'>❌ ID must be a number</h2><a href='/'>Go Back</a>"
        if IDs in savemessage:
            m = savemessage[IDs]
            return render_template("msge.html",message=m)
        return "<h2 style='color:red;'>❌ Invalid ID!</h2><a href='/'>Go Back</a>"



if __name__=="__main__":
    app.run(debug=True)


