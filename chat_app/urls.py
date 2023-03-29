from django.urls import path
from . import views

urlpatterns = [
   path("kirim",views.send_chat,name="kirim"),
   path("baca",views.read_chat,name="baca"),
   path("register",views.register,name="register")
]