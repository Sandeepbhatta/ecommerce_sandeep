from django.db import models

# Create your models here.
#request and response


class Brand(models.Model):
    name = models.CharField(max_length=200)


is_active = models.BooleanField()
