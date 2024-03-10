from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

# get API
url_data = "https://api.npoint.io/99c279bb173a6e28359c/data"
url_surat = "https://api.npoint.io/99c279bb173a6e28359c/surat/"
response_data = requests.get(url_data)
response_surat = requests.get(url_surat)

@app.route('/')
def index():
    daftar_surah = response_data.json()
    return render_template("index.html", data=daftar_surah)

@app.route('/surat/<int:surat_number>/<nama_surat>')
def get_surat_ayat(surat_number, nama_surat):
    # Ganti URL sesuai dengan endpoint yang diberikan
    url = f"https://api.npoint.io/99c279bb173a6e28359c/surat/{surat_number}"
    response = requests.get(url)

    if response.status_code == 200:
        surat_ayat = response.json()
        return render_template("surat.html", surat_ayat=surat_ayat, nama_surat=nama_surat)
    else:
        return "error : Surat not found"

if __name__ == "__main__":
    app.run(debug=True)
