from django.db import models
from task.models import taskModel

# Create your models here.
class catagoryModel(models.Model):
    catagoryName = models.CharField(max_length = 20)
    task = models.ManyToManyField(taskModel, default=None)
    
    def __str__(self):
        return self.catagoryName