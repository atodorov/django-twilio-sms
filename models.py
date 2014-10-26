from django.db import models

# Create your models here.

class SmsUser(models.Model):
    '''
        Information about users and their mobile numbers
    '''

    name = models.CharField(max_length=128, db_index=True)
    email = models.CharField(max_length=64, db_index=True)
    number = models.CharField(max_length=32, db_index=True)

    def __unicode__(self):
        return "%s %s" % (self.number, self.name)
