from django.contrib import admin
from celebrities import models
from celebrities.models import Cetegory, Teg

admin.site.register(models.Celebrity)
admin.site.register(models.Cetegory)
admin.site.register(models.Teg)