from rest_framework import serializers
from .models import allTeam, employee


class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employee
        fields= '__all__'

class allTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = allTeam
        fields= '__all__'

