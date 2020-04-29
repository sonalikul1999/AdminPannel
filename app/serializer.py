from rest_framework import serializers
from app.views import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = '__all__'