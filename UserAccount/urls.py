from knox import views as knox_views
from .views import LoginAPI,RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    #path('api/teacher_request/',RequestAPI.as_view(), name='request for teacher'),
]