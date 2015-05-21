from flask_admin.contrib.mongoengine import ModelView
# from flask_admin.form import rules
from wtforms import fields, widgets

# Define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()

class PostView(ModelView):
    form_overrides = dict(text=CKTextAreaField)
    column_filters = ['title', 'text']

    column_searchable_list = ('title', 'text')

    create_template = 'create.html'
    edit_template = 'edit.html'

class CategoryView(ModelView):
    column_filters = ['orderId']

class UserView(ModelView):
    meta = {
    }
