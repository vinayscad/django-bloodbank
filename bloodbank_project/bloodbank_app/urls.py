from django.urls import path
from .views import donor_list, add_donor,edit_donor,delete_donor

urlpatterns = [
    path('donors/', donor_list, name='donor_list'),
    path('donors/add/', add_donor, name='add_donor'),
    path('donors/edit/<int:donor_id>/', edit_donor, name='edit_donor'),
    path('donors/delete/<int:donor_id>/', delete_donor, name='delete_donor'),
]

