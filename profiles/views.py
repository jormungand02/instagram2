from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SavedPost

from .serializers import SavedPostSerializer
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
