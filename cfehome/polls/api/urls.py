from .views import BlogPostRudView, BlogPostAPIView
from django.urls import path


urlpatterns = [
    path('<int:id>/', BlogPostRudView.as_view(), name='post-rud'),
    path('', BlogPostAPIView.as_view(), name='post-create'),
]
