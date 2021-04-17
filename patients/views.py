from django.shortcuts import render,redirect
from django.http import HttpResponse
from patients.models import TaskList
from patients.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import csv
# Create your views here.

@login_required
def patients(request):
    if request.method == "POST":
         form = TaskForm(request.POST or None)
         if form.is_valid():
            instance=form.save(commit = False)
            instance.manage=request.user
            form.save()
         messages.success(request,("New patient Added!"))
         return redirect('patients')
    else:   
         all = TaskList.objects.filter(manage=request.user)
         paginator = Paginator(all,10)
         page = request.GET.get('pg')
         all=paginator.get_page(page)
         return render(request,'patient.html', {'all':all})

@login_required
def searchname(request):
    if request.method == "POST":
        name = request.POST['name']
        ans = TaskList.objects.filter(name__contains=name , manage=request.user)
        return render(request,'searchname.html',{'all':ans} )

    else:
        return render(request,'searchname.html', )

@login_required
def delete_patient(request,patient_id):
    patient = TaskList.objects.get(pk=patient_id)
    if patient.manage == request.user:
        patient.delete()
    else:
       messages.error(request,("Access Restricted, You are not Allowed.")) 
    
    return redirect('patients')

@login_required
def edit_patient(request,patient_id):
    if request.method == 'POST':
         patient = TaskList.objects.get(pk=patient_id)
         form = TaskForm(request.POST or None,instance = patient)
         if form.is_valid():
              form.save()
         messages.success(request,("Patient Data Edited!"))
         return redirect('patients')
    else:   
         patient_obj = TaskList.objects.get(pk=patient_id)
         return render(request,'edit.html', {'patient_obj':patient_obj})


@login_required
def contact(request):
    context = { 'welcome_text':'Hi Here are our contacts'}
    return render(request,'contact.html', context)



def index(request):
    context = { 'welcome_text':'Hi Here are our Index page'}
    return render(request,'index.html', context)




@login_required
def searchapp(request):
    if request.method == "POST":
        firstappointment = request.POST['firstappointment']
        ans = TaskList.objects.filter(firstappointment__contains=firstappointment,manage=request.user )
        return render(request,'searchapp.html',{'all':ans} )

    else:
        return render(request,'searchapp.html', )
    
@login_required
def searchnumber(request):
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        ans = TaskList.objects.filter(phone_number__contains=phone_number ,manage=request.user)
        return render(request,'searchnumber.html',{'all':ans} )

    else:
        return render(request,'searchnumber.html', )
    
    
@login_required
def searchdisease(request):
    if request.method == "POST":
        disease = request.POST['disease']
        ans = TaskList.objects.filter(disease__contains=disease ,manage=request.user)
        return render(request,'searchdisease.html',{'all':ans} )

    else:
        return render(request,'searchdisease.html', )
    

@login_required
def download_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=patients.csv'
    csv_writer = csv.writer(response)
    csv_writer.writerow(['Name','Disease','First-Appointment','phone_Number'])
    all = TaskList.objects.filter(manage=request.user)
    for obj in all:
        csv_writer.writerow([obj.name,obj.disease,obj.firstappointment,obj.phone_number])
    return response


