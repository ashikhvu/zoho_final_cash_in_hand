from rest_framework import serializers
from .models import CashInHandHistory

class CashInHandHistorySerializer(serializers.ModelSerializer):
    class Meta:
        models = CashInHandHistory
        fields = "__all__"

        # def __str__(self):
        #     return self.name