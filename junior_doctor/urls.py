from django.urls import path
from . import views

app_name = 'junior_doctor'

urlpatterns = [

    path('juniorDoctor_dashboard',views.juniorDoctor_dashboard,name='juniorDoctor_dashboard'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('juniorDoctor_appointmentList',views.juniorDoctor_appointmentList,name="juniorDoctor_appointmentList"),
    path('juniorDoctor_appointmentList_FilterbyDate',views.juniorDoctor_appointmentList_FilterbyDate,name="juniorDoctor_appointmentList_FilterbyDate"),
    path('juniorDoctor_patientDiagonise/<str:patient_id>/',views.juniorDoctor_patientDiagonise,name="juniorDoctor_patientDiagonise"),
    path('juniorDoctor_patientDiagonise_View_Edit/<str:patient_id>/',views.juniorDoctor_patientDiagonise_View_Edit,name="juniorDoctor_patientDiagonise_View_Edit"),
]
