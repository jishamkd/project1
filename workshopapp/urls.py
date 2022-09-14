
from django.urls import path

from workshopapp import views, managerviews, customerviews

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.login_view,name='loginpage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('managerdashboard',managerviews.managerdashboard,name='managerdashboard'),
    path('reg', customerviews.registration, name='reg'),
    path('customerdashboard', customerviews.customerdashboard,name='customerdashboard'),
    path('managerregistration', managerviews.managerreg, name='managerregistration'),
    path('managerslist',managerviews.viewmanagerlist, name='managerslist'),
    path('customerlist',customerviews.viewcustomerlist,name='customerlist'),
    path('customerupdate/<int:id>/',customerviews.customerupdate,name='customerupdate'),
    path('customerdelete/<int:id>/',customerviews.customerdelete,name='customerdelete'),
    path('managerupdate/<int:id>/',managerviews.managerupdate,name='managerupdate'),
    path('managerdelete/<int:id>/',managerviews.managerdelete,name='managerdelete'),
    path('feedback',views.feedback_form,name='feedback'),
    path('feedbackview',views.feedback_view,name='feedbackview'),
    path('reply/<int:id>/',views.reply_fun, name='reply'),
    path('cusfeedbackview',views.feedback_view_by_customer, name='cusfeedbackview'),
    path('replytomanager/<int:id>/',views.Manager_Admin_reply,name='replytomanager'),
    path('messagetoadmin',views.manager_message_form, name='messagetoadmin'),
    path('managermessageview',views.Manager_Message_View, name='managermessageview'),
    path('schedule',views.Schedule_View_by_Admin, name='schedule'),
    path('schedulecustomer',views.Schedule_View_by_Customer, name='schedulecustomer'),
    path('addschedule',views.scheduleadd,name='addschedule'),
    path('scheduledelete/<int:id>/',views.scheduledelete,name='scheduledelete')





]