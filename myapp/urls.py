from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_by/<str:pk>', views.post_by, name='post_by'),
]
