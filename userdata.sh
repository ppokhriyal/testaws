#!/bin/bash

sudo apt-get update
sudo apt-get -y install apache2
sudo ufw allow 'Apache'
sudo apt-get -y install python3
sudo apt-get -y install python3-pip
sudo apt-get -y install libapache2-mod-wsgi-py3
sudo pip3 install flask
sudo pip3 install Flask-SQLAlchemy
sudo mkdir -p /var/www/html/web
sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf
sudo rm -rf 00-default.conf
sudo mv app.wsgi /var/www/html/web/
sudo mv test /var/www/html/web/
sudo service apache2 restart

