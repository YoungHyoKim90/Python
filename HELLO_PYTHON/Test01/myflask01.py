from flask import Flask,jsonify, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return redirect("static/omok04_19.html")

if __name__ == '__main__':
    app.run(debug=True)