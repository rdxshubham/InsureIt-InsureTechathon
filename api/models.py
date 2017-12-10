from django.db import models


# Create your models here.

class TrueCallerData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=50, null=True)
    create_time = models.DateTimeField(null=True)

    def __str__(self):
        return '%s | %s | %s' % (self.id, self.name, self.create_time)


class TDITips(models.Model):
    id = models.AutoField(primary_key=True)
    tips = models.TextField()

    def __str__(self):
        return '%s ' % (self.id)
