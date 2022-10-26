from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from workshopapp.forms import registrationForm, loginform, managerregistration, Contact_Admin, work_assign
from workshopapp.models import manager, Manager_Contact_Admin, Appointment, Assign_Work, customer

@login_required(login_url='loginpage')
def managerdashboard(request):
    return render(request,'manager/manager.html')


@login_required(login_url='loginpage')
def managerreg(request):
    data = managerregistration()
    log = loginform()
    if request.method == 'POST':
        data = managerregistration(request.POST, request.FILES)
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


@login_required(login_url='loginpage')
def viewmanagerlist(request):
    data = manager.objects.all()
    return render(request, 'admin/workmanagersdetails.html', {"data":data})


@login_required(login_url='loginpage')
def managerupdate(request,id):
    data = manager.objects.get(id=id)
    form = managerregistration(instance=data)
    if request.method == 'POST':
        form = managerregistration(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('managerslist')
    return render(request, 'admin/managerupdate.html', {"form": form})


@login_required(login_url='loginpage')
def managerdelete(request,id):
    data= manager.objects.get(id=id)
    data.delete()
    return redirect('managerlist')


@login_required(login_url='loginpage')
def manager_message_form(request):
    form=Contact_Admin()
    u = request.user
    if request.method == 'POST':
        form = Contact_Admin(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.user=u
            data.save()
            return render(request, 'manager/manager.html')
    return render(request, 'manager/managerchatpage.html', {'form': form})


@login_required(login_url='loginpage')
def Admin_reply_view_to_manager(request):
    u = request.user
    data = Manager_Contact_Admin.objects.filter(user=u)
    return render(request, 'manager/adminreplyview.html', {'data': data})



@login_required(login_url='loginpage')
def Appointment_View_by_Manager(request):
    app = Appointment.objects.all()
    return render(request, 'manager/appointmentlist.html', {'app': app})


@login_required(login_url='loginpage')
def status_accept(request,id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment confirmed')
    return redirect('appointmentlist')


@login_required(login_url='loginpage')
def status_reject(request,id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment rejected')
    return redirect('appointmentlist')


@login_required(login_url='loginpage')
def Work_assign_View_by_manager(request):
    u = manager.objects.get(user=request.user)
    v = Assign_Work.objects.filter(manager=u)
    return render(request,'manager/workassignviewbymanager.html', {'v': v})


@login_required(login_url='loginpage')
def work_status_edit(request,id):
    data = Assign_Work.objects.get(id=id)
    form = work_assign(instance=data)
    if request.method == 'POST':
        form = work_assign(request.POST, instance=data)
        if form.is_valid():
           form.save()
           return redirect('workassignmanagerview')
    return render(request, 'manager/workstatusedit.html', {"form": form})



@login_required(login_url='loginpage')
def customerlist_view_by_manager(request):
    u = manager.objects.get(user=request.user)
    v = customer.objects.all()
    return render(request,'manager/customerslistviewbymanager.html', {'v': v})
