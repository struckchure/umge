sudo mv umge.conf /etc/apache2/sites-available/
sudo a2ensite umge.conf

sudo mv umge_frontend.conf /etc/nginx/sites-enabled/

sudo systemctl reload apache2 nginx
sudo systemctl restart apache2 nginx

sudo ufw reload
