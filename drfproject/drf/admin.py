from django.contrib import admin
from .models import Contact
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','title','email']

admin.site.register(Contact,ContactAdmin)
admin.site.register(get_user_model())