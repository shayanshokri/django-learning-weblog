from django.urls import path
from . import views

urlpatterns = [
    # path('', views.PostListView.as_view()),
    # path('<int:pk>/', views.PostDetailView.as_view())
    path('', views.PostView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', views.PostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
