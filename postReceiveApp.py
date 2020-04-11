import subprocess
from flask import Flask, abort, request
import json

app = Flask(__name__)  # Standard Flask app
# webhook = Webhook(app, endpoint="/postreceive")

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Why are you here? We use github webhooks to automate deployment here."

def _get_header(key):
    """Return message header"""

    try:
        return request.headers[key]
    except KeyError:
        abort(400, "Missing header: " + key)

# @webhook.hook()        # Defines a handler for the 'push' event
@app.route("/postreceive", methods = ['POST'])
def on_push():
    event_type = _get_header("X-Github-Event")
    content_type = _get_header("content-type")
    
    data = request.get_json()
    if data is None:
        abort(400, "Request body must contain json")
    

    completed = subprocess.run(["/home/ubuntu/GithubWebhook/githubupdate.sh"],  capture_output=True)
