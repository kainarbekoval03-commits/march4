from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Celebrity(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    image = models.ImageField(null=True, blank= True, upload_to="celebs")
    bio = models.TextField(verbose_name="Биография")
    birth_date = models.DateField(verbose_name="Дата рождения")
    content = models.TextField(null=True, blank=True)
    cetegory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tegs = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# Create your models here.
