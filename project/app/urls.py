from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('signup/',views.signup),
    path('content/',views.content),
    path('update/',views.update),
]