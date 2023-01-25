from django.db import models

# Create your models here.

class regmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)

# 02/12/2022  file upload: models.py,forms.py,views.py,file.html,urls.py

class filemodel(models.Model):
    itemname=models.CharField(max_length=20)
    image=models.FileField(upload_to='cbapp/static')
    def __str__(self):
        return self.itemname

    # def __str__(self):
    #     return self.image

# 08/12/2022

class newmodel(models.Model):
    catchoice=[
        ('kerala','kerala'),        # html pagil koduthekunna athe reethiyil thanne venam tuple nullil ividem kodukkan.
        ('karnataka','karnataka'),  # ithil first value('kerala') avide ninnu edukkunna datayum second value('kerala')
        ('tamilnadu','tamilnadu')   # models lekku pokunna datayum aanu.
    ]
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    state = models.CharField(max_length=20,choices=catchoice)


# work

class productmodel(models.Model):
    productname=models.CharField(max_length=20)
    price = models.IntegerField()
    customername=models.CharField(max_length=20)
    customerid=models.CharField(max_length=20)
    phone = models.IntegerField()
    # def __str__(self):
    #     return self.productname







