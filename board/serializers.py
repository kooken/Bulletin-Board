from phonenumber_field import serializerfields
from rest_framework import serializers

from board.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_image = serializers.ImageField(source="author.image", read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "text", "created_at", "author_id", "ad_id", "author_first_name", "author_last_name",
                  "author_image")


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "phone", "author_first_name", "author_last_name", "description",
                  "author_id")
