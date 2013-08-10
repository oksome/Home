# Run this after installing packages in 'apt-required'.


# Setting audio to use Jack output:
amixer cset numid=3 1

# Fixing encoding alert messages:
sudo echo "export LC_ALL=C" >> /etc/bash.bashrc

# Setting up music directory:
mkdir $HOME/music
sudo ln -s $HOME/music /var/lib/mpd/music/home
sudo vim /etc/mpd.conf
sudo service mpd restart

# Setting up web server:
mkdir $HOME/web
sudo cp ra.nginx /etc/nginx/sites-available/ra
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/ra ./
sudo rm default
cd -
sudo service nginx reload

mkdir -p $HOME/inbox/torrent/running
mkdir -p $HOME/inbox/torrent/complete

sudo chgrp debian-transmission $HOME/inbox/torrent/running
sudo chgrp debian-transmission $HOME/inbox/torrent/complete
chmod 770 $HOME/inbox/torrent/running
chmod 770 $HOME/inbox/torrent/complete

sudo usermod -a -G debian-transmission $USER
