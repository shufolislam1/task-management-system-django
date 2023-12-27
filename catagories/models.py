from django.db import models
from task.models import taskModel

# Create your models here.
class catagoryModel(models.Model):
    class Meta:
        catagoryName = models.CharField(max_length = 20)
        task = models.ManyToManyField(taskModel)
# hello

# hello 2
