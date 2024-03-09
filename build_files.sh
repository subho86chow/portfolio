python3.9 -m pip install -r requirements.txt

cp -r media/* staticfiles_build/media
python3.9 manage.py collectstatic --noinput --clear
