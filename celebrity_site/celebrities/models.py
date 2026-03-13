from django.db import models

class Celebrity(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    bio = models.TextField(verbose_name="Биография")
    birth_date = models.DateField(verbose_name="Дата рождения")

    def str(self):
        return self.name

# Create your models here.
