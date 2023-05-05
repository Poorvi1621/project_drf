from rest_framework import serializers
from .models import detailsForm
from django.db.models import fields


class detailSerializer(serializers.ModelSerializer):

    class Meta:
        model = detailsForm
        fields ='__all__'