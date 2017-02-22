from django.db import models


class Menu(models.Model):
    subject = models.CharField(max_length=100, blank=True, default='')
    image = models.URLField( default='')

    def __unicode__(self):
        return self.subject