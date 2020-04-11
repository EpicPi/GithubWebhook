#!/bin/bash

/usr/biin/ssh-agent -s
/usr/bin/ssh-add/ ~/id_rsa

cd /var/www/base
/usr/bin/git pull
cd /var/www/gyms
/usr/bin/git pull