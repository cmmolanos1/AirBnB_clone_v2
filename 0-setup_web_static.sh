#!/usr/bin/env bash

# Install nginX and configure the http header
sudo apt-get -y update
sudo apt-get -y install nginx
sudo sed -i "15i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf

# Create directories
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Create html file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Set-up the content of /data/web_static/current/ to redirect
# to domain.tech/hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
exit 0
