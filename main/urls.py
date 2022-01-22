from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('control-panel/', views.control, name="control"),
    path('login/', views.login, name="login"),
    path('details/<int:id>',views.details, name='details',)
]