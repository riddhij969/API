from rest_framework import serializers
# from rest_framework import users
from .models import users
# from NodeApp.models import Products

class usersSerializer(serializers.ModelSerializer):

    user_ID = serializers.IntegerField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    company_name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    zip = serializers.IntegerField(required=False)
    email = serializers.CharField(required=False)
    web = serializers.CharField(required=False)

    class Meta:
        model = users
        # fields = ('Name', 'Model_No')
        fields = '__all__'