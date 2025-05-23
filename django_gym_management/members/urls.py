from django.urls import path
from .views import MemberListCreateView, MemberDetailView,AllMembersView

urlpatterns = [
    path('', MemberListCreateView.as_view(), name='member-list'),
    path('<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('all/',AllMembersView.as_view(), name='member-all'),  # Add this endpoint
]
