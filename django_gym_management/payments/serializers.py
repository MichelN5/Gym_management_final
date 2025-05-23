from rest_framework import serializers
from .models import Bill, FeePackage


from django.contrib.auth import get_user_model

class FeePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePackage
        fields = '__all__'



class BillSerializer(serializers.ModelSerializer):
    from members.serializers import MemberSerializer  # Import your MemberSerializer
    member = MemberSerializer()
    class Meta:
        model = Bill
        fields = '__all__'


class BillSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
