from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=100, blank=True, default='')


    def __unicode__(self):
        return self.city_name