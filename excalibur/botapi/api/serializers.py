from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from botapi.models import Complaint, Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
        'category_id',
        'category'
        ]

class ComplaintDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = [
        'track_id',
        'username',
        'timestamp',
        'location',
        'description',
        'category',
        'category_id',
        'source',
        'image'
        ]

class ComplaintListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = 'botapi-api:detail')

    class Meta:
        model = Complaint
        fields = [
        'url',
        'track_id',
        'username',
        'timestamp',
        'location',
        'description',
        'category',
        # 'category_id',
        'source',
        'image'
        ]
