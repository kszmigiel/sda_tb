from django.urls import path
from .views import RentalListView, RentalDetailView, RentalCreateView, RentalUpdateView, RentalDeleteView

urlpatterns = [
    path('rentals/', RentalListView.as_view(), name='rentals'),
    path('rentals/<int:pk>/', RentalDetailView.as_view(), name='rental_detail'),
    path('rentals/create/', RentalCreateView.as_view(), name='rental_create'),
    path('rentals/<int:pk>/update/', RentalUpdateView.as_view(), name='rental_update'),
    path('rentals/<int:pk>/delete/', RentalDeleteView.as_view(), name='rental_delete'),
]