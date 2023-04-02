from django.urls import path,include
from .views import User,HelloView


urlpatterns = [
    path('', User.as_view(), name="user"),
    path("check/", HelloView.as_view(), name="Hello"),
    
]