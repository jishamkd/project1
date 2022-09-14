from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from workshopapp.forms import registrationForm, loginform
from workshopapp.models import customer


def registration(request):
    form = registrationForm()
    log = loginform()
    if request.method == 'POST':
        log = loginform(request.POST)
        form = registrationForm(request.POST)
        if form.is_valid() and log.is_valid():
            user = log.save(commit = False)
            user.is_customer = True
            user.save()
            user1 = form.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('loginpage')
    return render(request, 'customer/register.html', {'form': form,'log': log})

def customerdashboard(request):
    return render(request,'customer/cusdash.html')


def viewcustomerlist(request):
    form = customer.objects.all()
    return render(request, 'admin/customerdetails.html', {"form":form})

def customerupdate(request,id):
    data = customer.objects.get(id=id)
    form = registrationForm(instance=data)
    if request.method == 'POST':
        form = registrationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('customerlist')
    return render(request, 'admin/customerupdate.html', {"form": form})


def customerdelete(request,id):
    data= customer.objects.get(id=id)
    data.delete()
    return redirect('customerlist')




