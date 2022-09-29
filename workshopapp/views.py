from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from workshopapp.forms import feedbackForm, Contact_Admin, Admin_Shedule, work_assign
from workshopapp.models import feedback, Manager_Contact_Admin, Schedule, customer, Appointment, manager, Assign_Work


def homepage(request):
    return render(request,'homepage.html')


def loginpage(request):
    return render(request,'loginpage.html')

def dashboard(request):
    return render(request,'admin/dashboard.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('dashboard')
            if user.is_customer:
                return redirect('customerdashboard')
            if user.is_manager:
                return redirect('managerdashboard')
    return render(request,'loginpage.html')

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


def feedback_view(request):
    data = feedback.objects.all()
    return render(request, 'admin/customerfeedback.html',{'data': data})


def reply_fun(request,id):
    data = feedback.objects.get(id=id)
    if request.method=='POST':
        r = request.POST.get('reply')
        data.reply = r
        data.save()
        return redirect('feedbackview')
    return render(request, 'admin/reply.html',{'data': data})


def feedback_view_by_customer(request):
    u = request.user                      #details of login user saved to variable u
    data = feedback.objects.filter(user=u)
    return render(request, 'customer/cusfeedbackview.html', {'data': data})


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
    return render(request, 'admin/managerchatpage.html', {'form': form})


def Manager_Message_View(request):
    data = Manager_Contact_Admin.objects.all()
    return render(request, 'admin/managermessageview.html',{'data': data})



def Manager_Admin_reply(request,id):
    data = Manager_Contact_Admin.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        data.reply = r
        data.save()
        return redirect('managerdashboard')
    return render(request, 'admin/replytomanager.html', {'data': data})



def Admin_reply_view_to_manager(request):
    u = request.user
    data = Manager_Contact_Admin.objects.filter(user=u)
    return render(request, 'manager/adminreplyview.html', {'data': data})




def Schedule_View_by_Admin(request):
    data = Schedule.objects.all()
    return render(request, 'admin/schedule.html', {'data': data})


def Schedule_View_by_Customer(request):
    u = request.user                      #details of login user saved to variable u
    data = Schedule.objects.all()
    return render(request,'customer/scheduleviewbycustomer.html', {'data': data})


def scheduleadd(request):
    form = Admin_Shedule()
    if request.method == 'POST':
        form = Admin_Shedule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    return render(request, 'admin/scheduleupdate.html', {"form": form})


def scheduledelete(request,id):
    data= Schedule.objects.get(id=id)
    data.delete()
    return redirect('schedule')


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


def Appointment_View_by_Manager(request):
    app = Appointment.objects.all()
    return render(request, 'manager/appointmentlist.html', {'app': app})


def status_accept(request,id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment confirmed')
    return redirect('appointmentlist')


def status_reject(request,id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment rejected')
    return redirect('appointmentlist')


def Status_View_by_Customer(request):
    u = customer.objects.get(user=request.user)
    s = Appointment.objects.filter(user=u)
    return render(request, 'customer/statusviewbycustomer.html', {'s': s})


def work_assign_details(request):
    form = work_assign()
    if request.method == 'POST':
        form = work_assign(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return render(request, 'admin/dashboard.html')
    return render(request,'admin/workassign.html', {'form': form})


def Work_assign_View_by_admin(request):
    wrk = Assign_Work.objects.all()
    return render(request, 'admin/workassignlist.html', {'wrk': wrk})

def Work_assign_View_by_manager(request):
    u = manager.objects.get(user=request.user)
    v = Assign_Work.objects.filter(manager=u)
    return render(request,'manager/workassignviewbymanager.html', {'v': v})


def work_status_edit(request,id):
    data = Assign_Work.objects.get(id=id)
    form = work_assign(instance=data)
    if request.method == 'POST':
        form = work_assign(request.POST, instance=data)
        if form.is_valid():
           form.save()
           return redirect('workassignmanagerview')
    return render(request, 'manager/workstatusedit.html', {"form": form})


def Work_assign_View_by_customer(request):
    u = customer.objects.get(user=request.user)
    v = Assign_Work.objects.filter(customer=u)
    return render(request,'customer/workassignviewbycustomer.html', {'v': v})


def customerlist_view_by_manager(request):
    u = manager.objects.get(user=request.user)
    v = customer.objects.all()
    return render(request,'manager/customerslistviewbymanager.html', {'v': v})