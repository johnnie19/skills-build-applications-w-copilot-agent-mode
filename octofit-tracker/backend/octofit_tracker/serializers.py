from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    members = UserSerializer(many=True)

class ActivitySerializer(serializers.Serializer):
    user = UserSerializer()
    activity_type = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    user = UserSerializer()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
