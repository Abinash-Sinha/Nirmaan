# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_patient/', views.add_patient, name='add_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('', views.get_patients, name='get_patients'),
    path('view_patient/<int:patient_id>/', views.view_patient_details, name='view_patient'),
    path('patient/<int:patient_id>/representative/', views.view_representative, name='view_representative'),
    path('search/', views.search_patients, name='search_patients'),
]
