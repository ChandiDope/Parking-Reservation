from django.urls import path 
from . import views
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name='Home'),
    path("about/", AboutPageView.as_view(), name='About')
]
