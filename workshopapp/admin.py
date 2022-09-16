

# Register your models her
from django.contrib import admin

from workshopapp.models import Login, customer, manager, feedback, Manager_Contact_Admin, Schedule, Appointment

admin.site.register(Login)
admin.site.register(customer)
admin.site.register(manager)
admin.site.register(feedback)
admin.site.register(Manager_Contact_Admin)
admin.site.register(Schedule)
admin.site.register(Appointment)