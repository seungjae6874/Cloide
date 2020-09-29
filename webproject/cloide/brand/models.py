from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length= 100)
    bnum = models.IntegerField(primary_key=True)
    intro = models.TextField()
    url = models.TextField(max_length = 200)
    date = models.DateTimeField(null=True)
    logo = models.ImageField(blank = True, upload_to = "images",null = True)
    phone = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Agesex(models.Model):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    age = models.IntegerField()
    sex = models.IntegerField()

    def __str__(self):
        return self.brand.name

class Stylekind(models.Model):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    style = models.IntegerField()
    kind = models.IntegerField()

    def __str__(self):
        return self.brand.name




