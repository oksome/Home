# This script will install CMU PocketSphinx for voice control of the Pi.
# 
# Instructions originate from:
# https://sites.google.com/site/observing/Home/speech-recognition-with-the-raspberry-pi

sudo apt-get install python-dev

curl http://sourceforge.net/projects/cmusphinx/files/sphinxbase/0.8/sphinxbase-0.8.tar.gz/download > sphinxbase-0.8.tar.gz
curl http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/0.8/pocketsphinx-0.8.tar.gz/download > pocketsphinx-0.8.tar.gz

cd sphinxbase-*
sudo make uninstall
sudo make clean
./configure --enable-fixed --with-python
make
sudo make install

cd ../pocketsphinx-*
sudo make uninstall
sudo make clean
./configure --with-python
make
sudo make install
