from django.db import models

class Tag(models.Model):
     name = models.CharField(max_length=50, unique=True)
     def __str__(self):
        return self.name

# Create your models here.
class TodoData(models.Model):
    todotimestamp = models.DateTimeField(auto_now_add=True)
    todotitle = models.CharField(max_length=100, blank=False)
    tododescription = models.CharField(max_length=1000,  blank=False)
    tododate = models.DateField()
    todotag = models.ManyToManyField('Tag',blank=True)
    todostatus = models.CharField(max_length=1000,blank=False, choices=(
         ('OPEN','OPEN'),
         ('WORKING','WORKING'),
         ('PENDING REVIEW','PENDING REVIEW'),
         ('COMPLETED','COMPLETED'),
         ('OVERDUE','OVERDUE'),
         ('CANCELLED', 'CANCELLED')))
    
    def __str__(self):
        return self.todotitle
