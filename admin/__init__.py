import os
import os.path as op
import datetime
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin import Admin
from flask_admin.contrib import fileadmin
from admin import views

app = Flask(__name__, static_folder='uploads')
app.config["MONGODB_SETTINGS"] = {'DB': "rest"}
app.config["SECRET_KEY"] = ""

# Create models
db = MongoEngine(app)

class User(db.Document):
    CHOICES = ("active", "inactive")
    GENDER_CHOICES = ("", "male", "female")

    login = db.StringField(max_length=255, required=True)
    email = db.EmailField(max_length=255, required=True)
    password = db.StringField(max_length=255, required=True)
    # avatar = '',
    dateCreated = db.DateTimeField(default=datetime.datetime.now, required=True),
    status = db.ListField(db.StringField(choices=CHOICES))
    fio = db.StringField(max_length=255)
    country = db.StringField(max_length=255)
    sex = db.ListField(db.StringField(choices=GENDER_CHOICES))
    dateBirth = db.StringField(max_length=255)
    telephone = db.StringField(max_length=255)
    skype = db.StringField(max_length=255)

    def __unicode__(self):
        return self.login
    
class Category(db.Document):
    CHOICES = ("active", "inactive")

    title = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255)
    status = db.ListField(db.StringField(choices=CHOICES))
    orderId = db.IntField()

    def __unicode__(self):
        return self.title

class Post(db.Document):
    CHOICES = ("active", "inactive")

    dateCreated = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    textPreview = db.StringField(max_length=255, required=True)
    text = db.StringField(required=True)
    categoryId = db.ReferenceField(Category, required=True)
    userId = db.ReferenceField(User, required=True)
    image = db.StringField(max_length=255)
    source = db.URLField(max_length=255)
    status = db.ListField(db.StringField(choices=CHOICES))
    hasVideo = db.BooleanField()

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': False,
        'indexes': ['dateCreated', 'slug'],
        'ordering': ['-created_at']
    }

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

path = op.join(op.dirname(__file__), 'uploads')
try:
    os.mkdir(path)
except OSError:
    pass

admin = Admin(app, name='Adminka')
admin.add_view(views.PostView(Post, name="Posts"))
admin.add_view(views.CategoryView(Category, name="Categories"))
admin.add_view(views.UserView(User, name="Users"))
admin.add_view(fileadmin.FileAdmin(path, '/uploads/', name='Files'))