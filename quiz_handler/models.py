from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.
class Pool(models.Model):
    id_pool = models.AutoField(primary_key=True, default=0)
    text_pool = models.CharField(max_length=250)

class Choice(models.Model):
    id_var = models.AutoField(primary_key=True, default=0)
    id_poll = ForeignKey(Pool, on_delete=models.CASCADE, related_query_name='choices')
    text_var = models.CharField(max_length=200)
    count_votes = models.IntegerField(default=0)
        