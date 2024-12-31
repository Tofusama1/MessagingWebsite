from rest_framework.serializers import ModelSerializer
from ..models import Post
# Django format into jason format so that we can send it over to the web 
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')