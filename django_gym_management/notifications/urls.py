from django.urls import path
from .views import NotificationListCreateView, NotificationListView

urlpatterns = [
    path('', NotificationListCreateView.as_view(), name='notifications'),
    path('all/', NotificationListView.as_view(), name='notification-list'),
]
