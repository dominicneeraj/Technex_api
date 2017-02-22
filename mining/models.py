from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    image = models.URLField()

    def __unicode__(self):
        return self.name

class Chapter(models.Model):
    subject = models.ForeignKey(Subject)
    chapter_title=models.CharField(max_length = 200, unique = True)


    def __unicode__(self):
        return self.chapter_title

class Content(models.Model):
    chapter_title=models.ForeignKey(Chapter)

    content =models.TextField()
    image = models.URLField( default='',blank=True)

    def __unicode__(self):
       return unicode(self.chapter_title)


