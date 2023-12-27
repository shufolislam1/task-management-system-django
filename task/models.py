from django.db import models
from catagories.models import catagoryModel

# Create your models here.

class taskModel(models.Model):
    taskTitle = models.CharField(max_length=20)
    taskDescription = models.TextField()
    taskCatagories = models.ManyToManyField(catagoryModel, default=None)
    is_completed = models.BooleanField(default=False)
    taskAssignedDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.taskTitle