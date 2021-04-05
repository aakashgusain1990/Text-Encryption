from django.db import models

class AllData(models.Model):
    passkey = models.CharField(max_length=200)
    encrytext = models.TextField()
    
    def __str__(self):
        return self.passkey

class ImgData(models.Model):
    imgpasskey = models.CharField(max_length=200)
    encryptimg = models.ImageField(upload_to='images/')
    decryptimg = models.ImageField(upload_to='images/',default=None)

    def __str__(self):
        return self.imgpasskey

    



# Create your models here.
