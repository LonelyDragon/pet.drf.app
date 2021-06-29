from django.db.models import fields
from quiz_handler.models import Pool
from rest_framework import serializers

class PoolResultSerialazer(serializers.Serializer):
    id_var = serializers.CharField()
    text_var = serializers.CharField(max_length = 200)
    count_votes = serializers.IntegerField()

class CreatePoolSerialazer(serializers.ModelSerializer):
    
    text_var = serializers.SlugRelatedField(
        queryset = []
        many=True,
        slug_field='text_var'
    )

    class Meta:
        model = Pool
        fields ['text_pool', 'text_var']
    
    def create(self, validated_data):
        text_var = validated_data
        