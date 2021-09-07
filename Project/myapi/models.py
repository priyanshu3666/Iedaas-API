from django.db import models

# Create your models here.
class employee(models.Model):
    f_name=models.CharField(max_length=20)
    l_name= models.CharField(max_length=20)
    e_id = models.IntegerField()


    def __str__(self):
        return self.f_name

class allTeam(models.Model):
    id=models.CharField(max_length=30,primary_key=True) 
    teamName=models.CharField(max_length=30)
    winningYears=models.CharField(max_length=30)
    venue = models.CharField(max_length=80)

    def __str__(self):
        return self.teamName