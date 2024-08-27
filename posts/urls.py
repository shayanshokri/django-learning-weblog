from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.PostView, basename='posts')

urlpatterns = [
    # path('', views.PostListView.as_view()),
    # path('<int:pk>/', views.PostDetailView.as_view())
    # path('', views.PostView.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # path('<int:pk>/', views.PostView.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # }))
    path('', include(router.urls))
]
