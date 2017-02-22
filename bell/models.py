from django.db import models


class City(models.Model):
    name = models.CharField(max_length = 200, unique = True)

    image = models.URLField(blank=True)

    lat=models.DecimalField(max_digits=20,decimal_places=10,unique=True)
    lng=models.DecimalField(max_digits=20,decimal_places=10,unique=True)
    def __unicode__(self):
        return self.name





class Restra(models.Model):
    city=models.ForeignKey(City ,default='')
    area = models.CharField(max_length = 200, unique = False,blank=True)
    image = models.URLField(blank=True)
    restra_name=models.CharField(max_length = 200, unique = True)
    lat=models.DecimalField(max_digits=20,decimal_places=10,unique=True)
    lng=models.DecimalField(max_digits=20,decimal_places=10,unique=True)


    def __unicode__(self):
        return self.restra_name

class Deal(models.Model):
    restra_name=models.ForeignKey(Restra)

    content =models.TextField()
    val=models.DecimalField(max_digits=20,decimal_places=10)

    def __unicode__(self):
       return unicode(self.content)
