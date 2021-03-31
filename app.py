from flask import Flask, render_template, request, send_from_directory, redirect, send_file
from pytube import YouTube

app = Flask(__name__)

mode = 'dev'

if mode == 'dev':
    app.debug = True
else:
    app.debug = False

UPLOAD_DIRECTORY = './videos'

def download(url):
    yt = YouTube(url)
    print("Title:",yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download(UPLOAD_DIRECTORY)
    return yt.title

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/geturl')
def fetchurl():
    url = request.args['url']
    title = download(url)
    print(title+'.mp4')
    return redirect('/test/'+title+".mp4")
    # return send_from_directory(UPLOAD_DIRECTORY,title+".mp4")

@app.route('/test/<url>')
def test(url):
    print(url)
    # url = url.replace("%20", " ")
    print(url)
    # return send_from_directory(UPLOAD_DIRECTORY,url)
    return send_file(UPLOAD_DIRECTORY+'/'+url, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0')