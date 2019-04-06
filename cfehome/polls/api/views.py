from polls.models import BlogPost
from rest_framework import generics
from .serializers import BlogPostSerializers


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BlogPostSerializers
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
        # pk = self.kwargs.get("pk")
        # return BlogPost.objects.get(pk=pk)
