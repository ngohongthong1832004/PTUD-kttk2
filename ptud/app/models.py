from django.db import models

class CV(models.Model):
    name = models.CharField(max_length=5000)
    email = models.CharField(max_length=5000)
    education = models.CharField(max_length=5000)
    work_experience = models.CharField(max_length=5000)
    skill = models.CharField(max_length=5000)
    def __str__(self):
        return self.name
    
    
    
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=5000)
    def __str__(self):
        return self.title