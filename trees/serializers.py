from rest_framework import serializers

from .models import Tree

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','planter','description', 'created_at')
        model = Tree
        