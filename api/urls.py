from django.urls import path
from .views import like_management
from .views import aprove_management

urlpatterns = [
    path('like_photo', like_management.LikeManager.as_view()),
    path('aprove_photo', aprove_management.aproveManagement.as_view())
    ]