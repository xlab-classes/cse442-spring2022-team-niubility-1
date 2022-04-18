from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from app.main.models import *
def create_admin(app):

    flask_admin = Admin()
    flask_admin.init_app(app)
    mymodels = [(User, 'User Management'), (Task, 'Task')]
    for model in mymodels:
        flask_admin.add_view(ModelView(model[0], db.session, name=model[1], category='System Management'))