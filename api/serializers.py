from rest_framework import serializers

from .models import Client,Project


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
            'created_at',
        ),
        fields = (
            'id',
            'name',
            'phone',
            'author',
            'email',
            'created_at',
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        read_only_fields = (
            'created_at',
        ),
        fields = (
            'id',
            'title',
            'description',
            'status',
            'author',
            'client',
            'slug',
            
        )
        