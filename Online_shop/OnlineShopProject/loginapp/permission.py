from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get(app_label='auth', model='user')
permission = Permission.objects.create(codename='can_watch_factor', name='Can watch factor', content_type=content_type)