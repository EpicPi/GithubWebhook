# GithubWebhook
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
```
mkdir env
python3 -m venv env/bin/activate
source env
pip install wheel
pip install uwsgi flask github-webhook
deactivate
````
make systemd unit file

```
[Unit]
Description=uWSGI instance for github webhook autodeploy
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/GithubWebhook
Environment="PATH=/home/ubuntu/GithubWebhook/env/bin"
ExecStart=/home/ubuntu/GithubWebhook/env/bin/uwsgi --ini GithubWebhook.ini

[Install]
WantedBy=multi-user.target
```

add new nginx conf
```
server {
    listen 80;
    server_name webhook.trueshape.io;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/ubuntu/GithubWebhook/postreceive.sock;
    }
}
```