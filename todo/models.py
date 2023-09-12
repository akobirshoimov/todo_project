from django.db import models
from datetime import datetime
# Create your models here.

class TodoModel(models.Model):
    task_name = models.CharField(max_length=100, default= ' ')
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=True)
    desc = models.TextField(default='no info')
    
    def __str__(self) -> str:
        return self.task_name
    
