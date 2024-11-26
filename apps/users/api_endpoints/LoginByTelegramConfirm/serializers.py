from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from apps.users.models import OneTimeCode
from .utils import get_tokens_for_user

User = get_user_model()

class LoginByTelegramConfirmSerializer(serializers.Serializer):
    code = serializers.CharField()

    def create(self, validated_data):
        one_time_code = validated_data["code"]
        otp = OneTimeCode.objects.filter(code=one_time_code).last()

        if otp and otp.is_expired():

            raise ValidationError({
                "error": "otp_is_expired",
                "message": "OTP is expired. Retry again."
            })
        
        if not otp:
            raise ValidationError({
                "error": "not_found",
                "message": "OTP not found"
            })
        
        
        user = User.objects.get(username=otp.phone_number)
        return get_tokens_for_user(user)
        