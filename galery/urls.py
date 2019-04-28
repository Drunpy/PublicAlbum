from django.urls import path
from .views import home
from .views import galery
from .views import administration


urlpatterns =[
    path('', home.index, name="index"),
    path('galery', galery.read),
    path('upload_image', galery.upload, name="upload_image"),
    path('administration/login', administration.adm_login, name="adm_login"),
    path('administration/aprove_photos', administration.aprove, name="aprove_photos"),
]