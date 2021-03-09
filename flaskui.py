from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/trans")
def translate():
    return "Translation page"
app.run(debug=True)