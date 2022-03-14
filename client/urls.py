from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('homepage/', views.client_home, name='client'),
    path('test/', views.client_test, name='test'),
    path('delete-app/<int:delid>/', views.delete_appointment, name='apdelete'),
    path('staff-in-time/', views.in_time, name='timing'),
    path('staf-out-time/<int:upout>/', views.out_time, name='out'),
    path('staff-out-times/<int:upoutx>/', views.change_out_time, name='outx'),
    path('local-appointment/', views.local_app, name='local'),
    path('delet_upcomming/<int:updele>/',
         views.upcomeing_delete, name='upcome_delete'),
    path('get-local-app/', views.view_localapp, name='getlocal'),
    path('delete-local/<int:ldel>/', views.local_delete, name='lodel'),
    path('send-mail/', views.send_myemail, name='sendm'),
    path('customer-feedback/', views.feedback, name='feed'),
    path('update-my-staff/<int:stup>/', views.staff_update, name='update_staff'),
    path('get-my-staff/', views.get_staff_update, name='get_staff'),
    path('delete-staff/<int:rst>/', views.delete_staff, name='delst'),
    path('remove-staff/', views.get_delete_staff, name='staff_del'),
    path('get-feedback/', views.view_feedback, name="feedback"),
    path('delete-feed/<int:fld>/', views.delete_feedback, name='delfeed'),
    path('read-feedback/<int:re>/', views.read_feedback, name='read'),
    path('my-service/', views.service, name='service'),
    path('staff-today-work/', views.today_work, name='today_work'),
    path('get-today-work/<str:sname>/', views.get_today_work, name='twork'),
    path('last-month-work/<str:ssname>/',
         views.last_month_data, name='month_work'),
    path('staff-month-work/', views.month_work, name='lastmon'),
    path('get-smooth-data/', views.get_smooth, name='smooth'),
    path('staff-salary/', views.staff_salary, name='salary'),
    path('salary-data/', views.salary_data, name='salary_data'),
    path('product-data/', views.product_file, name='product'),
    path('timeing-report/', views.time_report, name='report'),
    path('today-time-report/', views.today_time_work, name='totime'),
    path('get-month-records/<str:rec>/',
         views.display_timing_rec, name='get_rec'),
    path('pay-advance-salary/', views.advanced_salary, name='payad'),
    path('get-salary-data/<str:get_sl>/',
         views.get_month_salary, name='get_salary'),
    path('new-packages/', views.create_packages, name='create_package'),
    path('sales-records/', views.customers_records, name='pro_rec'),


    path('reset-password/', auth_view.PasswordResetView.as_view(
        template_name="client/password_reset.html"), name='password_reset'),
    path('reset-password-done/', auth_view.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset-password-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password-complete/', auth_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
