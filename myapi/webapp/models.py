from django.db import models

class employees(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.name

