from django.db import models

class detailsForm(models.Model):
    
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=20)
    Country=models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.Name
