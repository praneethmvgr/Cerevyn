from rest_framework import serializers

class LogSerializer(serializers.Serializer):
    time = serializers.CharField()
    status = serializers.CharField()

class DashboardSerializer(serializers.Serializer):
    logs = LogSerializer(many=True)
    metrics = serializers.ListField()