from django.contrib import admin

from .models import *
admin.site.register(Category)
admin.site.register(Stuff)
admin.site.register(Entry)
