from django.db import models

# Create your models here.
class Lists(models.Model):
    name = models.CharField(max_length = 500)
    tasks = models.CharField(max_length = 2000)
    priority = models.CharField(max_length=100)
    time = models.CharField(max_length=20)

    def __str__ (self):
        return self.name + "- "+ self.tasks

class Assignmments(models.Model):
    assignment = models.ForeignKey(Lists, on_delete= models.CASCADE )
    class_name = models.CharField(max_length = 2000)
     #Lists, on_delete = models.CASCADE)
