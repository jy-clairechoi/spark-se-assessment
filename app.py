# import os
# # import sys

# import coverage
# COV = coverage.coverage(
#     branch=True,
#     include='project/*',
#     omit=[
#         'project/tests/*',
#         'project/server/config.py',
#         'project/server/*/__init__.py'
#     ]
# )
# COV.start()

# from project.server import app, db#, models
# from project.server.models import User

# import click
# from flask import Flask, make_response, jsonify
# from flask_migrate import Migrate

# migrate = Migrate(app, db)

# @app.route("/")
# def root_site():
#     return "<p>It works!</p>"

# @app.route("/users/index")
# def user_list():
#     users = []
#     for user in User.query.all():
#         users.append({
#             "admin": user.admin,
#             "email": user.email,
#             "id": user.id,
#             "registered_on": user.registered_on
#         })
#     responseObject = {"users": users}
#     return make_response(jsonify(responseObject)), 201

# from project.server.auth.views import auth_blueprint
# app.register_blueprint(auth_blueprint)

# @app.cli.command()
# @click.option('--coverage/--no-coverage', default=False,
#                 help='Run tests under code coverage.')
# def test(coverage):
#     """Run the unit tests."""
#     if coverage and not os.environ.get('FLASK_COVERAGE'):
#         import subprocess
#         os.environ['FLASK_COVERAGE'] = '1'
#         sys.exit(subprocess.call(sys.argv))

#     import unittest
#     """Runs the unit tests without test coverage."""
#     tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         if COV:
#             COV.stop()
#             COV.save()
#             print('Coverage Summary:')
#             COV.report()
#             basedir = os.path.abspath(os.path.dirname(__file__))
#             covdir = os.path.join(basedir, 'tmp/coverage')
#             COV.html_report(directory=covdir)
#             print('HTML version: file://%s/index.html' % covdir)
#             COV.erase()
#         return 0
#     return 1

# if __name__ == '__main__':
#     app.run()