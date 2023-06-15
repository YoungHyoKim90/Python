from flask import Flask,jsonify, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/static/examples/_ex01.html")

if __name__ == '__main__':
    app.run(debug=True)