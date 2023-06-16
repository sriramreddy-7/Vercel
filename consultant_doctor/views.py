from django.shortcuts import render

from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,logout,login
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages

from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_control
from django.http import HttpResponseRedirect
from patient.models import PatientPrimaryData,FT
# Create your views here.

def consultantDoctor_dashboard(request):
    patient_count=PatientPrimaryData.objects.count()
    appt_count=FT.objects.count()
    return render(request,'consultantDoctor_dashboard.html',{'patient_count':patient_count,'appt_count':appt_count})

@cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie('sessionid')
    return response

def consultantDoctor_patientList(request):
    patient=PatientPrimaryData.objects.all()
    return render(request,'consultantDoctor_patientList.html',{'patient':patient})

def consultantDoctor_appointmentList(request):
    patient=FT.objects.all()
    return render(request,'consultantDoctor_appointmentList.html',{'patient':patient})


























