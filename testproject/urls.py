from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),

    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view()),

    path('', views.RegisterUserAPIView.as_view()),
]
