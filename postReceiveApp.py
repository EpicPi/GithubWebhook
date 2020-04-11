import subprocess
from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app, endpoint="/postreceive")

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Why are you here? We use github webhooks to automate deployment here."

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    # subprocess.run(["sh"," ~/GithubWebhook/githubupdate.sh"])
    subprocess.run(["exit 1"])
