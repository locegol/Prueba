from django.conf.urls import url
from .views import home,post_list
from . import views

urlpatterns = [
    url('home', post_list),
    url('post/new/', views.newpost,name="newpost")
]