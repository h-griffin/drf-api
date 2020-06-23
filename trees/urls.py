from django.urls import path
from .views import TreesList, TreesDetail

urlpatterns = [
    path('', TreesList.as_view(), name='trees_list'),
    path('<int:pk>/', TreesDetail.as_view(), name='trees_detail'),
]