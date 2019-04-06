from .views import BlogPostRudView
from django.urls import path


urlpatterns = [
    path('<int:id>/', BlogPostRudView.as_view(), name='post-rud'),
]
