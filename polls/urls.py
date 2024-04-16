from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("tender_detail/", views.tender_detail, name="tender_detail"),
    path('user/', views.user, name="user"),
    path('signin/', views.signin, name="signin"),
    path('signout', views.signout, name='signout'),
    path('notify/<int:pk>', views.notify, name="notify"),
    path('tenderer/', views.tenderer)
]