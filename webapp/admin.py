from django.contrib import admin
from .models import User, WebAppMeta

# Register your models here.
admin.site.register(User)
admin.site.register(WebAppMeta)
