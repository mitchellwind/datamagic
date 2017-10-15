from django.db import models

# Create your models here.


class Mydata(models.Model):

    item_list = models.CharField(max_length=200)
    freq = models.CharField(max_length=20, null=True, blank=True)
    method = models.CharField(max_length=20, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):

        return self.item_list
