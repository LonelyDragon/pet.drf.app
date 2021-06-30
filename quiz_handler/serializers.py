from quiz_handler.models import Pool, Choice
from rest_framework import serializers

class PoolResultSerializer(serializers.Serializer):
    id_var = serializers.CharField()
    text_var = serializers.CharField(max_length = 200)
    count_votes = serializers.IntegerField()


class PoolInfoSerializer(serializers.ModelSerializer):
    choices = serializers.SlugRelatedField(many=True, slug_field='text_var', queryset=Choice.objects.all())
    class Meta:
        model = Pool
        fields = (
            'text_pool',
            'choices'
        )

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        pool = Pool.objects.create(**validated_data)
        Choice.objects.create(pool=pool, **choices)
        return pool

class ChoiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = (
            'text_var',
        )