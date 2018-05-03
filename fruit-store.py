from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

import time

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = request.form["strawberry"]
    raspberry = request.form["raspberry"]
    blackberry = request.form["blackberry"]
    apple = request.form["apple"]
    fruits = {"strawberry":strawberry,"raspberry":raspberry,"blackberry":blackberry,"apple":apple}

    fname = request.form["first_name"]
    lname = request.form["last_name"]
    student_id = request.form["student_id"]

    items = int(strawberry) + int(raspberry) + int(blackberry) + int(apple)

    localtime = time.asctime( time.localtime(time.time()) )

    return render_template("checkout.html", fruits=fruits, fname=fname, lname=lname, student_id=student_id, items=items, localtime=localtime)

@app.route('/fruits')         
def fruits():
    fruits = ["apple.png", "blackberry.png", "raspberry.png", "strawberry.png"]
    return render_template("fruits.html", fruits=fruits)

if __name__=="__main__":   
    app.run(debug=True)    