
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('maps', crud1),
    path('table', crud2),
    path('table/<int:id>', crud2Update),
    path('table/hapus/<int:id>', crud2Hapus),
    path('login', login),

    path('register', register),
    path('logout', keluar),
]
