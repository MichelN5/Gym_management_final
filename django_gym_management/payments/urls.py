from django.urls import path
from .views import *

urlpatterns = [
    path('fee-packages/', FeePackageListCreateView.as_view(), name='fee-package-list-create'),
    path('fee-packages/<int:pk>/', FeePackageRetrieveUpdateDeleteView.as_view(), name='fee-package-detail'),
    path('fee-packages/all/', FeePackageListView.as_view(), name='fee-package-get-all'), 
    #BILLS
    path('bills/', BillListCreateView.as_view(), name='bill-list-create'),
    path('bills/<int:pk>/', BillRetrieveUpdateDeleteView.as_view(), name='bill-retrieve-update-delete'),
    path('bills/all/', BillListView.as_view(), name='bill-public-list'),  # Optional public endpoint

     path('bills/user/<int:user_id>/', UserBillListView.as_view(), name='user-bills'),
]
