from flask import Flask, render_template
import requests

app = Flask(__name__)

#get api
url = "https://api.npoint.io/99c279bb173a6e28359c/data"
response = requests.get(url).json()

@app.route('/')
def index():
    datas = response
    return render_template("index.html", datas=datas)

if __name__ == "__main__":
    app.run(debug=True)