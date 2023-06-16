from django.urls import path
from . import views

app_name = 'hospital_admin'

urlpatterns = [

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('logout_view',views.logout_view,name="logout_view"),

]