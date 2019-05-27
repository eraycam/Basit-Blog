from django.contrib import admin
from django.urls import path
from . import views
app_name = "user"

urlpatterns = [
    
    path('kayitol/',views.kayitol,name="kayitol"),
    path('giris/',views.giris,name="giris"),
    path('cikis/',views.cikis,name="cikis"),
]