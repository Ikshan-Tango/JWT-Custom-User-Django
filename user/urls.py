from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.HelloView.as_view(), name="Hello")

]