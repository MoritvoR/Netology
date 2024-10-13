from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name
