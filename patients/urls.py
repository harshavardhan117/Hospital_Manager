from django.urls import path
from patients import views

urlpatterns = [
    path('', views.patients,name='patients'),
    path('delete/<patient_id>', views.delete_patient,name='delete_patient'),
    path('edit/<patient_id>', views.edit_patient,name='edit_patient'),
    path('download',views.download_data,name='download'),
    
    path('searchname',views.searchname,name = 'searchname'),
    path('searchdisease',views.searchdisease,name = 'searchdisease'),
    path('searchapp',views.searchapp,name = 'searchapp'),
    path('searchnumber',views.searchnumber,name = 'searchnumber'),
]