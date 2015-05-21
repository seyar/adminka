from flask.ext.admin import Admin, BaseView, expose

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

    @expose('/test/')
    def test(self):
        return self.render('test.html')

class AnotherAdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('anotheradmin.html')
