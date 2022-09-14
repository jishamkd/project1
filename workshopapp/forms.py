import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TimeInput

from workshopapp.models import Login, customer, manager, feedback, Manager_Contact_Admin, Schedule


class loginform(UserCreationForm):
    class Meta:
        model=Login
        fields = ('username','password1','password2')

class registrationForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        exclude=('user',)

class managerregistration(forms.ModelForm):
    class Meta:
        model=manager
        fields = '__all__'
        exclude = ('user',)

class DateInput(forms.DateInput):
     input_type = "date"

class feedbackForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=feedback
        fields = ('date','feedback')
        exclude = ('user','reply')


class Contact_Admin(forms.ModelForm):
    class Meta:
        model = Manager_Contact_Admin
        fields = '__all__'
        exclude = ('user','reply')


class TimeInput(forms.TimeInput):
    input_type = "time"



class Admin_Shedule(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = Schedule
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")
        date = cleaned_data.get("date")
        if start > end:
            raise forms.ValidationError("End Time should be greater than start Time.")
        if date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past")
        return cleaned_data






