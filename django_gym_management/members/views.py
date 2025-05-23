from rest_framework import generics, permissions
from .models import Member
from .serializers import MemberSerializer, MemberSerializerCreate
from rest_framework.permissions import IsAuthenticated
from django_gym_management.permissions import IsSuperUser


class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializerCreate
    permission_classes = [IsAuthenticated, IsSuperUser]  # Require authentication & superuser access

class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializerCreate
    permission_classes = [IsAuthenticated, IsSuperUser]  # Require authentication & superuser access

class AllMembersView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]  # Require authentication & superuser access
