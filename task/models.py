from django.db import models

# Create your models here.

class taskModel(models.Model):
    taskTitle = models.CharField(max_length=20)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignedDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.taskTitle