from django.urls import path, include
from .views import PostViewSet

urlpatterns = [
    path('profile/', PostViewSet.as_view({'get': 'list'})),
    path('profile/<int:pk>/', PostViewSet.as_view({'get': 'retrieve'})),
    # Добавьте другие маршруты, если нужно
]
