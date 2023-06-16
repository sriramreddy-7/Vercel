from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'receptionist'

urlpatterns = [
    path('receptionist_dashboard',views.receptionist_dashboard,name='receptionist_dashboard'),
    path('logout_view',views.logout_view,name="logout_view"),
    path('newPatient_registration',views.newPatient_registration,name="newPatient_registration"),
    path('oldPatient_registration',views.oldPatient_registration,name="oldPatient_registration"),
    path('patient_Acknowledgment/<str:patient_id>/',views.patient_Acknowledgment,name="patient_Acknowledgment"),
    path('appointment/<str:patient_id>/',views.appointment,name="appointment"),
    path('receptionist_patientList',views.receptionist_patientList,name="receptionist_patientList"),
    path('receptionist_appointmentList',views.receptionist_appointmentList,name="receptionist_appointmentList"),
    path('receptionist_patient_View_Edit/<str:patient_id>/',views.receptionist_patient_View_Edit,name="receptionist_patient_View_Edit"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




