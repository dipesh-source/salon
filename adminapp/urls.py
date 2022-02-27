from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/',views.homepage,name='home'),
    path('sign-out/',views.logout_view,name='logoutv'),
    path('update-client/<int:uid>/',views.update_client,name='myclient'),
    path('give-access/',views.give_access,name='access'),
    path('extends-access/<int:upacc>/',views.update_access,name='up_access'),
    path('delete_access/<int:del_data>/',views.delete_access_data,name='del_acc'),
]