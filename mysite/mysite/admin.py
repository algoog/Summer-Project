# myapp/admin.py

from django.contrib import admin
from .models import Person, House

admin.site.register(Person)
admin.site.register(House)
