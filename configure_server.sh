sudo cp ~/home/mohammed/umge/umge.conf /etc/apache2/sites-available/
sudo a2ensite umge.conf

sudo systemctl restart apache2
sudo systemctl reload apache2

# sudo mv umge_frontend.conf /etc/nginx/sites-enabled/

# sudo systemctl reload apache2 nginx
# sudo systemctl restart apache2 nginx

# sudo ufw reload
