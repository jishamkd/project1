from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from workshopapp.forms import feedbackForm, Contact_Admin, Admin_Shedule
from workshopapp.models import feedback, Manager_Contact_Admin, Schedule


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
        return redirect('managermessageview')
    return render(request, 'admin/replytomanager.html', {'data': data})


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

