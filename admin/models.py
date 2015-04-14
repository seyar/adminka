# import datetime
# from flask import url_for
# from admin import db

# class Post(db.Document):
#     dateCreated = db.DateTimeField(default=datetime.datetime.now, required=True)
#     title = db.StringField(max_length=255, required=True)
#     slug = db.StringField(max_length=255, required=True)
#     textPreview = db.StringField(max_length=255, required=True)
#     text = db.StringField(required=True)
#     # categoryId: 'a23rsd2fsd13r32rgsre42',
#     # userId: '12sd3rfsd23r23r',
#     image = db.StringField(max_length=255)
#     source = db.StringField(max_length=255)
#     status = db.StringField(max_length=255)
#     hasVideo = db.StringField(max_length=2)
#
#     # def get_absolute_url(self):
#     #     return url_for('post', kwargs={"slug": self.slug})
#
#     def __unicode__(self):
#         return self.title
#
#     meta = {
#         'allow_inheritance': False,
#         'indexes': ['dateCreated', 'slug'],
#         'ordering': ['-created_at']
#     }


# class Comment(db.EmbeddedDocument):
#     created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
#     body = db.StringField(verbose_name="Comment", required=True)
#     author = db.StringField(verbose_name="Name", max_length=255, required=True)
