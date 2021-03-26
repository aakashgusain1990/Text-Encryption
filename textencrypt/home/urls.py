from django.urls import path
from .views import (
    home, 
    encryption,
    decryption,
    encrypted,
    decrypted,
)
urlpatterns = [
    # path('', include('home.urls')),
    path('',home, name='home'),
    path('encryption/',encryption, name='encrypt'),
    path('decryption/',decryption,name='decrypt'),
    path('encrypted/',encrypted, name='encrypted'),
    path('decrypted/',decrypted,name='decrypted'),
    

]
