from django.contrib import admin
from celebrities import models
from celebrities.models import Category, Tag

admin.site.register(models.Celebrity)
admin.site.register(models.Category)
admin.site.register(models.Tag)