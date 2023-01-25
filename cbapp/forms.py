from django import forms
from django.contrib.auth.models import User
from .models import *

# what is ModelForm?
# it is a regular form which can automatically generate certain fields.The fields that are generates depends upon
# the content of meta class.
# what is Meta class?
# Meta class is an inner class of form class.It is used to change the behaviour of your form field.

# model upayogichu form ne generate cheyyum.athinanu ModelForm use cheyyunnathu.
# what is __all__ constructor?
# all is a field indicates that all fields in model should be included in forms.__all__ that returns a list of
# model fields.
# ie,models le field kale ellam form il include cheyyan __all__ use cheyyunnu.__all__ koduthal ella fields um list
# aayi kittum.

class regform(forms.ModelForm):
    class Meta:
        model=regmodel
        fields='__all__'
        #[name,email,password]

# 30/11/2022

class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)


# 1/12/2022

# registration step-by-step :1)forms.py , 2)views.py , 3)reg.html , 4)urls.py il path kodukkukka

class reg(forms.ModelForm):
    class Meta:
        model = User   # User ivde kitanam engil etavum mukalil "from django.contrib.auth.models import User"
        fields = ["username", "email", "password"]


# User:  from django.contrib.auth.models import User
# User model vechu form ne create cheythu.avashyamulla field kale list aaki.ini views.py il ponam.
#####

# login step-by-step :1)forms.py , 2)views.py , 3)lo.html , 4)urls.py il path kodukkukka

class lo(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)


# 02/12/2022

class fileform(forms.ModelForm):
    class Meta:
        model=filemodel
        fields='__all__'


# model aayittu user aanu upayogikkunnathengil list kodukkan sremikkuka.But ivide model aayittu filemodel use
# cheythathu kond '__all__' aanu use cheyyendathu.filemodel nammal aayittu thanne create cheyyunnathu kondu ella
# field kaleyum use cheyyan pattunnathu kond '__all__' use cheyyam.


#############################################################################################################

# work

class productform(forms.ModelForm):
    class Meta:
        model = productmodel
        fields ='__all__'


class plogform(forms.Form):
    customername = forms.CharField(max_length=20)
    customerid = forms.CharField(max_length=20)












###############################################################################################################
# 08/12/2022
# new class create cheyyumbol munpu create cheytha fn aayi match akan padilla.

class newreg(forms.Form):
    name=forms.CharField(max_length=20)     # name ennathu regb.html il <in ty le name= nu nere koduthekkunna same name.
    address=forms.CharField(max_length=200)         # address ennathu <textarea kullil name= nu nere koduthekkunna name.
    gender=forms.CharField(max_length=20)
    state=forms.CharField(max_length=20)







