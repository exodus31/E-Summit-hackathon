from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup', views.signup, name="signup"),
    path('signup_ent', views.signup_ent, name="signup_ent"),
    path('signup_inv', views.signup_inv, name="signup_inv"),
]