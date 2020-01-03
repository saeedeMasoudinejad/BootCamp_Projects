from django.contrib import admin
from .models import User, Food, CommentUser

admin.site.register(User)
admin.site.register(Food)
admin.site.register(CommentUser)
