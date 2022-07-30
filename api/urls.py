from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('client/<int:pk>/', ClientDetail.as_view(), name='detailcreate'),
    path('client/', ClientList.as_view(), name='listcreate'),
    path('client/search/', ClientListDetailfilter.as_view(), name='postsearch'),
# project urls
    path('project/<str:pk>/', ProjectDetail.as_view(), name='detailcreate'),
    path('project/', ProjectList.as_view(), name='listcreate'),
    path('project/search/', ProjectListDetailfilter.as_view(), name='postsearch'),
]
