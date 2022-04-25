from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from post.models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .permissions import OwnerOrReadOnly

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [OwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Post.objects.all()
            return queryset
        else:
            return Post.objects.filter(reader_role='all')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RegisterView(APIView):
    http_method_names = ['post']
    
    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            user = User(
                email = serializer.data['email']
            )
        
            try:
                validate_password(serializer.data['password'], user)
            except ValidationError as e:
                return Response(str(e), status=HTTP_400_BAD_REQUEST)
            User.objects.create_user(**serializer.validated_data)
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
