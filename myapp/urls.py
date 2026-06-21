from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('register/',views.user_register, name="register"),
    path('password_reset/',views.password_reset_request, name="password_reset"),
    path('password_reset_confirm/',views.password_reset_confirm, name="password_reset_confirm"),
    path('password_reset_done/',views.password_reset_done, name="password_reset_done"),
    path('password_reset_complete/',views.password_reset_complete, name="password_reset_complete"),
    path('',views.home, name="home"),
    path('expense/',views.expense_list, name="expense_list"),
    path('expense/create',views.expense_create, name="expense_create"),
    path('expense/delete',views.expense_delete, name="expense_delete"),
    path('expense/update',views.expense_update, name="expense_update"),
    path('expense/update',views.expense_update, name="expense_update"),
  
    
]
