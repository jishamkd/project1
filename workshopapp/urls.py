
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
    path('customerslistviewbymanager',managerviews.customerlist_view_by_manager,name='customerslistviewbymanager'),
    path('customerupdate/<int:id>/',customerviews.customerupdate,name='customerupdate'),
    path('customerdelete/<int:id>/',customerviews.customerdelete,name='customerdelete'),
    path('managerupdate/<int:id>/',managerviews.managerupdate,name='managerupdate'),
    path('managerdelete/<int:id>/',managerviews.managerdelete,name='managerdelete'),
    path('feedback',customerviews.feedback_form,name='feedback'),
    path('feedbackview',views.feedback_view,name='feedbackview'),
    path('reply/<int:id>/',views.reply_fun, name='reply'),
    path('cusfeedbackview',customerviews.feedback_view_by_customer, name='cusfeedbackview'),
    path('replytomanager/<int:id>/',views.Manager_Admin_reply,name='replytomanager'),
    path('messagetoadmin',managerviews.manager_message_form, name='messagetoadmin'),
    path('managermessageview',views.Manager_Message_View, name='managermessageview'),
    path('adminreplyview',managerviews.Admin_reply_view_to_manager,name='adminreplyview'),
    path('schedule',views.Schedule_View_by_Admin, name='schedule'),
    path('schedulecustomer',customerviews.Schedule_View_by_Customer, name='schedulecustomer'),
    path('addschedule',views.scheduleadd,name='addschedule'),
    path('scheduledelete/<int:id>/',views.scheduledelete,name='scheduledelete'),
    path('appointment/<int:id>/',customerviews.schedule_appointment,name='appointment'),
    path('appointmentlist',managerviews.Appointment_View_by_Manager, name='appointmentlist'),
    path('accept/<int:id>/',managerviews.status_accept, name= 'accept'),
    path('reject/<int:id>/', managerviews.status_reject, name= 'reject'),
    path('statusviewcustomer',customerviews.Status_View_by_Customer, name= 'statusviewcustomer'),
    path('workassign',views.work_assign_details,name='workassign'),
    path('workassignlist',views.Work_assign_View_by_admin,name='workassignlist'),
    path('workassignupdate/<int:id>/',views.work_assignlist_update,name='workassignupdate'),
    path('workassigndelete/<int:id>/',views.work_assignlist_delete,name='workassigndelete'),
    path('workassignmanagerview',managerviews.Work_assign_View_by_manager,name='workassignmanagerview'),
    path('workassignstatusedit/<int:id>/',managerviews.work_status_edit,name='workassignstatusedit'),
    path('workassigncustomerview',customerviews.Work_assign_View_by_customer,name='workassigncustomerview'),
    path('pay/<int:id>/',views.payment,name='pay'),
    path('logout',views.Logout, name='logout'),
    path('paymentcustomerview/<int:id>/',customerviews.payment_customerview,name='paymentcustomerview')






]