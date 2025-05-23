from django.shortcuts import redirect
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json


# Get user model
User = get_user_model()

# Function to generate JWT tokens with additional claims
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    # Add custom claims
    refresh["is_superuser"] = user.is_superuser
    refresh["is_staff"] = user.is_staff
    
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Only allow admins to see all users

    def get_object(self):
        return self.request.user
    

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Public access (Optional)
    
    
class UserDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        # Prepare user data
        user_data = {
            'id': user.id,
            'username': user.username,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,  # Ensure this is included
            'is_active': user.is_active
        }

        return Response(user_data)

@login_required
def google_login_callback(request):
    user = request.user

    social_accounts = SocialAccount.objects.filter(user=user)
    social_account = social_accounts.first()

    if not social_account:
        return redirect('http://localhost:5173/login/callback/?error=NoSocialAccount')
    
    token = SocialToken.objects.filter(account=social_account, account__provider='google').first()

    if token:
        # Generate JWT tokens with additional claims
        tokens = get_tokens_for_user(user)
        return redirect(f'http://localhost:5173/login/callback/?access_token={tokens["access"]}')
    else:
        return redirect(f'http://localhost:5173/login/callback/?error=NoGoogleToken')

@csrf_exempt
def validate_google_token(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            google_access_token = data.get('access_token')

            if not google_access_token:
                return JsonResponse({'detail': 'Access Token is missing.'}, status=400)
            return JsonResponse({'valid': True})
        except json.JSONDecodeError:
            return JsonResponse({'detail': 'Invalid JSON.'}, status=400)
    return JsonResponse({'detail': 'Method not allowed.'}, status=405)
