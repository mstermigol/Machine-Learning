from django.db import models
from platform import architecture

# Create your models here.
class mlModels(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    architecture = models.FileField(upload_to='mlmodels/') #json
    weights = models.FileField(upload_to='mlmodels/') #h5 file
    priority = models.PositiveSmallIntegerField(null=True)