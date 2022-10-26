from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from workshopapp.forms import feedbackForm, Contact_Admin, Admin_Shedule, work_assign, Payment_Form
from workshopapp.models import feedback, Manager_Contact_Admin, Schedule, customer, Appointment, manager, Assign_Work, \
    Payment

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



@login_required(login_url='loginpage')
def feedback_view(request):
    data = feedback.objects.all()
    return render(request, 'admin/customerfeedback.html',{'data': data})

@login_required(login_url='loginpage')
def reply_fun(request,id):
    data = feedback.objects.get(id=id)
    if request.method=='POST':
        r = request.POST.get('reply')
        data.reply = r
        data.save()
        return redirect('feedbackview')
    return render(request, 'admin/reply.html',{'data': data})


@login_required(login_url='loginpage')
def Manager_Message_View(request):
    data = Manager_Contact_Admin.objects.all()
    return render(request, 'admin/managermessageview.html',{'data': data})


@login_required(login_url='loginpage')
def Manager_Admin_reply(request,id):
    data = Manager_Contact_Admin.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        data.reply = r
        data.save()
        return redirect('managermessageview')
    return render(request, 'admin/replytomanager.html', {'data': data})


@login_required(login_url='loginpage')
def Schedule_View_by_Admin(request):
    data = Schedule.objects.all()
    return render(request, 'admin/schedule.html', {'data': data})


@login_required(login_url='loginpage')
def scheduleadd(request):
    form = Admin_Shedule()
    if request.method == 'POST':
        form = Admin_Shedule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    return render(request, 'admin/scheduleupdate.html', {"form": form})

@login_required(login_url='loginpage')
def scheduledelete(request,id):
    data= Schedule.objects.get(id=id)
    data.delete()
    return redirect('schedule')


@login_required(login_url='loginpage')
def work_assign_details(request):
    form = work_assign()
    if request.method == 'POST':
        form = work_assign(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return render(request, 'admin/dashboard.html')
    return render(request,'admin/workassign.html', {'form': form})

@login_required(login_url='loginpage')
def Work_assign_View_by_admin(request):
    wrk = Assign_Work.objects.all()
    return render(request, 'admin/workassignlist.html', {'wrk': wrk})



@login_required(login_url='loginpage')
def work_assignlist_update(request,id):
    data = Assign_Work.objects.get(id=id)
    form = work_assign(instance=data)
    if request.method == 'POST':
        form = work_assign(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('workassignlist')
    return render(request, 'admin/workassignlistupdate.html', {"form": form})

@login_required(login_url='loginpage')
def work_assignlist_delete(request,id):
    data = Assign_Work.objects.get(id=id)
    data.delete()
    return redirect('workassignlist')


# def payment_status(request,id):
#     n = Assign_Work.objects.get(id=id)
#     n.rep_category = 'Payment Done'
#     n.save()
#     messages.info(request, 'Payment Success')
#     return redirect('workassignlist')
#
#
# def payment_function(request):
#     form = Payment_Form()
#     if request.method == 'POST':
#         form = Payment_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('workassignlist')
#     return render(request, 'admin/payment.html', {"form": form})

@login_required(login_url='loginpage')
def payment(request,id):
    data = Assign_Work.objects.get(id=id)
    form = Payment_Form(instance=data)
    if request.method == 'POST':
        form = Payment_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            data.rep_category='Payment Done'
            data.save()
        return redirect('workassignlist')
    return render(request, 'admin/payment.html', {"form": form})



def Logout(request):
    # logout(request)
    return redirect('loginpage')



