from rest_framework import generics
from .models import FeePackage, Bill
from .serializers import FeePackageSerializer, BillSerializer,BillSerializerCreate
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django_gym_management.permissions import IsSuperUser
class FeePackageListCreateView(generics.ListCreateAPIView):
    queryset = FeePackage.objects.all()
    serializer_class = FeePackageSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]  # Require authentication & superuser access

class FeePackageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeePackage.objects.all()
    serializer_class = FeePackageSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]  # Require authentication & superuser access

class FeePackageListView(generics.ListAPIView):
    queryset = FeePackage.objects.all()
    serializer_class = FeePackageSerializer
    permission_classes = [AllowAny]  # Public access (Optional)

#Payments

class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializerCreate
    permission_classes = [IsAuthenticated, IsSuperUser]  # Require authentication & superuser access

class BillRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializerCreate
    permission_classes = [IsAuthenticated, IsSuperUser]  # Require authentication & superuser access

class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [AllowAny]  # Public access (Optional)

class UserBillListView(generics.ListAPIView):
    serializer_class = BillSerializer
    permission_classes = [AllowAny]  # Public access (Optional)

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        # Filter bills by user through the member relationship
        return Bill.objects.filter(member__user_id=user_id)
