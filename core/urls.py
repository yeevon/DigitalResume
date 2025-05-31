from django.urls import path
from .views import home, fun

urlpatterns = [
    path('', home),  # homepage shows Hello, World
    path('fun', fun),  # homepage shows Hello, World
]