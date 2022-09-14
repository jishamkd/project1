from django.shortcuts import render, redirect

from workshopapp.forms import registrationForm, loginform, managerregistration
from workshopapp.models import manager


def managerdashboard(request):
    return render(request,'manager/manager.html')

def managerreg(request):
    data = managerregistration()
    log = loginform()
    if request.method == 'POST':
        data = managerregistration(request.POST)
        log = loginform(request.POST)
        if log.is_valid() and data.is_valid():
            user = log.save(commit=False)
            user.is_manager = True
            user.save()
            user1 = data.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('loginpage')
    return render(request, 'manager/register.html', {'data': data, 'log': log})


def viewmanagerlist(request):
    data = manager.objects.all()
    return render(request, 'admin/workmanagersdetails.html', {"data":data})

def managerupdate(request,id):
    data = manager.objects.get(id=id)
    form = managerregistration(instance=data)
    if request.method == 'POST':
        form = managerregistration(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('managerslist')
    return render(request, 'admin/managerupdate.html', {"form": form})


def managerdelete(request,id):
    data= manager.objects.get(id=id)
    data.delete()
    return redirect('managerlist')





