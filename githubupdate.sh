#!/bin/bash

eval `/usr/bin/ssh-agent` > /dev/null 
ssh-add ~/.ssh/id_rsa

cd /var/www/base
git pull origin/master
cd /var/www/gyms
git pull origin/gym-landing-page