from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('posts', views.post_list),
    path('post/<int:pk>', views.post_details),
    path('post/create/', views.post_create),
]
