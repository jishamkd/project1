from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from workshopapp.forms import registrationForm, loginform, feedbackForm, Payment_Form
from workshopapp.models import customer, feedback, Schedule, Appointment, Assign_Work



def registration(request):
    form = registrationForm()
    log = loginform()
    if request.method == 'POST':
        log = loginform(request.POST)
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid() and log.is_valid():
            user = log.save(commit = False)
            user.is_customer = True
            user.save()
            user1 = form.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('loginpage')
    return render(request, 'customer/register.html', {'form': form,'log': log})

@login_required(login_url='loginpage')
def customerdashboard(request):
    return render(request,'customer/cusdash.html')


@login_required(login_url='loginpage')
def viewcustomerlist(request):
    form = customer.objects.all()
    return render(request, 'admin/customerdetails.html', {"form":form})


@login_required(login_url='loginpage')
def customerupdate(request,id):
    data = customer.objects.get(id=id)
    form = registrationForm(instance=data)
    if request.method == 'POST':
        form = registrationForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('customerlist')
    return render(request, 'admin/customerupdate.html', {"form": form})


@login_required(login_url='loginpage')
def customerdelete(request,id):
    data= customer.objects.get(id=id)
    data.delete()
    return redirect('customerlist')

@login_required(login_url='loginpage')
def feedback_form(request):
    form=feedbackForm()
    u = request.user
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.user=u
            data.save()
            return render(request, 'customer/cusdash.html')
    return render(request, 'customer/feedback.html', {'form': form})


@login_required(login_url='loginpage')
def feedback_view_by_customer(request):
    u = request.user                      #details of login user saved to variable u
    data = feedback.objects.filter(user=u)
    return render(request, 'customer/cusfeedbackview.html', {'data': data})


@login_required(login_url='loginpage')
def Schedule_View_by_Customer(request):
    u = request.user                      #details of login user saved to variable u
    data = Schedule.objects.all()
    return render(request,'customer/scheduleviewbycustomer.html', {'data': data})


@login_required(login_url='loginpage')
def schedule_appointment(request,id):
    data = Schedule.objects.get(id=id)
    u = customer.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u, schedule=data)
    if appointment.exists():
        messages.info(request, 'You have already requested appointment for this schedule')
        return redirect('schedulecustomer')
    else:
        if request.method == 'POST':
           obj = Appointment()
           obj.user = u
           obj.schedule = data
           obj.save()
           messages.info(request, 'Appointment added successfully')
           return redirect('schedulecustomer')
    return render(request, 'customer/appointment.html', {"data": data})


@login_required(login_url='loginpage')
def Status_View_by_Customer(request):
    u = customer.objects.get(user=request.user)
    s = Appointment.objects.filter(user=u)
    return render(request, 'customer/statusviewbycustomer.html', {'s': s})


@login_required(login_url='loginpage')
def Work_assign_View_by_customer(request):
    u = customer.objects.get(user=request.user)
    v = Assign_Work.objects.filter(customer=u)
    return render(request,'customer/workassignviewbycustomer.html', {'v': v})


@login_required(login_url='loginpage')
def payment_customerview(request,id):
    data = Assign_Work.objects.get(id=id)
    u = customer.objects.get(user=request.user)
    v = Assign_Work.objects.filter(customer=u)
    form = Payment_Form(instance=data)
    if request.method == 'POST':
        form = Payment_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            data.rep_category='Payment Done'
            data.save()
        return redirect('workassigncustomerview')
    return render(request, 'admin/payment.html', {"form": form})
