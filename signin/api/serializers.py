from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer , Serializer
from account.api import serializers
from signin.models import Profile

class ProfileSerializer(ModelSerializer):
    class Meta :
        model = Profile
        fields = ('Brand' , 'Plaque','Address','City')
class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta :
        model = User
        fields = '__all__'
    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        profile_serializer = ProfileSerializer(instance.profile,data=profile)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)


class ChangePasswordSerializer(Serializer):
    old_password = serializers.serializers.CharField(required=True)
    new_password = serializers.serializers.CharField(required=True)

    # Şifrenin güçlü olmasını istiyoruz
    def validate_new_password(self, value):
        validate_password(value)
        return value