import subprocess
from flask import Flask, abort, request
import json

app = Flask(__name__)  

@app.route("/")
def hello_world():
    return "Why are you here? We use github webhooks to automate deployment here."

def _get_header(key):
    try:
        return request.headers[key]
    except KeyError:
        abort(400, "Missing header: " + key)

@app.route("/postreceive", methods = ['POST'])
def on_push():
    event_type = _get_header("X-Github-Event")
    content_type = _get_header("content-type")
    
    data = request.get_json()
    if data is None:
        abort(400, "Request body must contain json")
    
    completed = subprocess.run(["sh","/home/ubuntu/GithubWebhook/githubupdate.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not completed.returncode == 0:
        abort(400, completed.stderr.decode('utf-8')) 
    
    return completed.stdout

