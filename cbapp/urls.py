from django.urls import path
from .views import *


urlpatterns=[
    path('register/',register.as_view(),name='register'),
    path('login/',login.as_view(),name='login'),

    # register
    path('regclass',regclass.as_view(),name='regclass'),

    # login
    path('logclass',logi.as_view(),name='logclass'),

    # display
    path('disp',dis.as_view(),name='disp'),

    # delete
    path('del/<pk>',re.as_view(),name='del'),      # pk :primary key,class based view il update/edit,delete
                                                   # detail iva cheyumbol url nte koode <pk> koodi pass cheyyanam.
                                                   # eppozhum use cheyyunna primary key, id aanu.
    # detail
    path('detail/<pk>',detail.as_view(),name='detail'),   # detail um single data ne matram ayathu kond <pk>
                                                          # pass cheyyanam.

    # update/edit
    path('up/<pk>',up.as_view(),name='up'),

#################################################################

    # file upload
    path('file',fileclass.as_view(),name='file'),

    # file display
    path('filedis',filedis.as_view(),name='filedis'),

    # file delete
    path('filedelete/<pk>',filedelete.as_view(),name='filedelete'),

    # file detail
    path('filedetail/<pk>',filedetail.as_view(),name='filedetail'),

    # file update
    path('fileup/<pk>',fileup.as_view(),name='fileup'),



    # 06/12/2022    index cheythirikkunnathu fn based aanu.
    path('index/',index),

    # 08/12/2022
    path('regview/',regview),




    # work path

    path('product/',product.as_view(),name='product'),
    path('plogin/',plogin.as_view(),name='plogin'),

    # display
    path('pdisp/',pdis.as_view(),name='pdisp'),

    # delete
    path('pdel/<pk>',pre.as_view(),name='pdel'),

    # detail
    path('pdetail/<pk>',pdetail.as_view(),name='pdetail'),

    # update/edit
    path('pup/<pk>',pup.as_view(),name='pup')




]

# class based use cheyyumbol path kodukkumbol views le classname.as_view enna reethiyil kodukkanam.
# path('register/',register.as_view(),name='register') ithil name='' ullil,url nu koduthirikkunna peru enthano
# (path nullil first koduthekkunnathu) athu thanne aayirikkanam '' lum kodukkendathu.

# as_view():as_view() is a class method which will connect view class with its url.