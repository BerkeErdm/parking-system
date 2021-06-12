from rest_framework import serializers
from account.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = {
            'fullName',
            'username',
            'email',
            'password',
            'confirmPassword',
            'slug',
        }

        model = Account
        fields = '__all__'
