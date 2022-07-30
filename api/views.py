from django.shortcuts import get_object_or_404


# Create your views here.
# Create your views here.
from .models import Client,Project
from .serializers import ClientSerializer,ProjectSerializer
from rest_framework import generics
from rest_framework import filters

from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class PostUserWritePermission(BasePermission):
    message = 'Editing Fields is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Client.objects.order_by('-created_at')
    serializer_class = ClientSerializer
    pagination_class = None

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Client.objects.order_by('-created_at')
    serializer_class = ClientSerializer

class ClientListDetailfilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.order_by('-created_at')
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name','^email']

class ProjectList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Project.objects.order_by('-created_at')
    serializer_class = ProjectSerializer
    pagination_class = None
    lookup_field = 'slug'

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    serializer_class = ProjectSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Project, slug=item)

class ProjectListDetailfilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.order_by('-created_at')
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title','completed']