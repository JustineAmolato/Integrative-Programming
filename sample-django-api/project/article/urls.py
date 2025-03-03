from django.urls import path
from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView    


urlpatterns = [
    path('article/', ArticleListCreateAPIView.as_view(), name='list-create-post'),
    path('article/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-delete-article')
]