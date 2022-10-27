from rest_framework import serializers
from . import models

class HngSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HngSlackDetails
        fields = ('slackUsername', 'backend', 'age', 'bio')

