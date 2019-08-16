from rest_framework import serializers
from movies.models import DoubanMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubanMovie
        fields = ['id', 'title', 'img_url', 'rate', 'detail_url']

# class MovieSerializer(serializers.Serializer):
#     movie_id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     img_url = serializers.URLField()
#     rate = serializers.DecimalField(max_digits=3, decimal_places=1)
#     detail_url = serializers.URLField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.img_url = validated_data.get('img_url', instance.img_url)
#         instance.rate = validated_data.get('rate', instance.rate)
#         instance.detail_url = validated_data.get(
#             'detail_url', instance.detail_url)

#         instance.save()
#         return instance
