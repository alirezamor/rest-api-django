from rest_framework import serializers
from polls.models import BlogPost


class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = [
            'user'
        ]

        def validate_title(self, value):
            qs = BlogPost.objects.filter(title__iexact=value)
            if qs.exist():
                raise serializers.ValidationError("The title must be unique")
            return value
