from django.urls import path
from . import views
  
urlpatterns = [
    # path('', include('home.urls')),
    path('',views.home, name='home'),
    path('encrypt/',views.encrypt, name='encrypt'),
    path('decrypt/',views.decrypt,name='decrypt'),
    path('encrypted/',views.encrypted, name='encrypted'),
    path('decrypted/',views.decrypted,name='decrypted'),
    path('imgencrypt/',views.imgencrypt,name='imgencrypt'),
    path('imgdecrypt/',views.imgdecrypt,name='imgdecrypt'),
    path('imgencrypted/',views.imgencrypted,name='imgencrypted'),
    path('imgdecrypted/',views.imgdecrypted,name='imgdecrypted'),

]
