from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog' #namespace

urlpatterns = [
   path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name="detail")
]
