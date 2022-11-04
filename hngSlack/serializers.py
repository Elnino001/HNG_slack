from rest_framework import serializers
from . import models

class HngSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HngSlackDetails
        fields = ('slackUsername', 'backend', 'age', 'bio')

class ArithmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Arithmetic
        fields = ("operation_type", "x", "y",)

