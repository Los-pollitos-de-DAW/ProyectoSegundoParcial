from django.urls import path
from . import views

urlpatterns = [
    path('rol', views.RolList.as_view()),
    path('rol/<int:pk>/',views.RolDetail.as_view()),
]