# from flask import Flask
# import datetime
# import flask_admin as admin
# from flask.ext.admin import Admin, BaseView, expose
# from flask_admin.form import rules
# from flask.ext.mongoengine import MongoEngine
# from flask_admin.contrib.mongoengine import ModelView
# from models import Post

# class MyView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('index.html')
#
#     @expose('/test/')
#     def test(self):
#         return self.render('test.html')
#
# class AnotherAdminView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('anotheradmin.html')

# Customized admin views
# class UserView(ModelView):
#     column_filters = ['name']
#
#     column_searchable_list = ('name', 'password')
#
#     form_ajax_refs = {
#         'tags': {
#             'fields': ('name',)
#         }
#     }

# class PostView(ModelView):
#     column_filters = ['slug']
#
#     column_searchable_list = ('title', 'text')

    # form_subdocuments = {
    #     'inner': {
    #         'form_subdocuments': {
    #             None: {
    #                 # Add <hr> at the end of the form
    #                 'form_rules': ('title', 'text', 'image', rules.HTML('<hr>')),
    #                 'form_widget_args': {
    #                     'title': {
    #                         'style': 'color: red'
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }

# @app.route('/')
# def index():
#     return '<a href="/admin/">Click me to get to Admin!</a>'


# admin = Admin(app, name='My App')
# admin.add_view(PostView(Post, name="Posts"))
# if __name__ == '__main__':

    # admin.add_view(MyView(name="view1", category='Test'))
    # admin.add_view(MyView(name="view1", category='Test'))
    # admin.add_view(AnotherAdminView(name="another"))


    # Start app
    # app.run()