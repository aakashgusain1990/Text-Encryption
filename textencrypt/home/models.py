from django.db import models

class AllData(models.Model):
    passkey = models.CharField(max_length=200)
    encrytext = models.TextField()
    
    def __str__(self):
        return self.passkey

    



# Create your models here.
