<<<<<<< HEAD
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic
=======
echo " BUILD START"
sudo apt-get install build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev
wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz
tar -xvf Python-3.10.4.tgz
cd Python-3.10.4
./configure --enable-optimizations --with-ensurepip=install
make -j $(nproc)
sudo make altinstall
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END" 
>>>>>>> 9ed4628 (last commit)
