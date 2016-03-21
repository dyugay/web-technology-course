sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello
sudo ln -s /home/box/web/etc/qa.py /etc/gunicorn.d/qa
sudo /etc/init.d/gunicorn start
sudo service mysql start

