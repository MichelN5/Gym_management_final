from rest_framework import serializers
from .models import Member
from payments.serializers import FeePackageSerializer
class MemberSerializer(serializers.ModelSerializer):
    fee_package = FeePackageSerializer() 
    class Meta:
        model = Member
        fields = '__all__'

class MemberSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
