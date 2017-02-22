from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 200, unique = False)
    contact=models.IntegerField(max_length=20,unique=True)
    image = models.URLField()

    def __unicode__(self):
        return self.name