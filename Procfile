web: gunicorn project.server:app
heroku ps:scale web=1
release: python ./project/server/__init__.py db update

