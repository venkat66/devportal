from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Developers(models.Model):
    username = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)
    picture = models.FileField(upload_to='images/',null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.username


class EchoData(models.Model):
    aid = models.CharField(max_length=250,null=True)
    lat = models.CharField(max_length=100,null=True)
    log = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=100,null=True)
    data = models.TextField()

    def __str__(self):
        return self.data

    class Meta:
        db_table = 'Gps_data'
