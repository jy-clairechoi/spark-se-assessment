web: gunicorn app:app
heroku ps:scale web=1
release: python flask db upgrade

