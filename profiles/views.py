from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import SavedPost, Profile
from .serializers import SavedPostSerializer, ProfileSerializer
from posts.serializers import PostSerializer
from posts.models import Post

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.objects.all()
    
class SavedViewSet(ModelViewSet):
    serializer_class = SavedPostSerializer

    def get_queryset(self):
        return Post.objects.all()


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Возвращаем профиль текущего аутентифицированного пользователя
        return self.request.user.profile