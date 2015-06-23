import os.path as op
from flask import url_for
from flask_admin.contrib.mongoengine import ModelView
from jinja2 import Markup
from flask.ext.admin import form
# from flask_admin.form import rules
from wtforms import fields, widgets

file_path = op.join(op.dirname(__file__), 'uploads')

# Define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()

class PostView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.image)))

    form_overrides = dict(text=CKTextAreaField)
    column_formatters = {
        'image': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'image': form.ImageUploadField('Image',
                                      base_path=file_path,
                                      thumbnail_size=(100, 100, True))
    }

    column_filters = ['title', 'text']

    column_searchable_list = ('title', 'text')

    create_template = 'create.html'
    edit_template = 'edit.html'

class CategoryView(ModelView):
    column_filters = ['orderId']

class UserView(ModelView):
    meta = {
    }

