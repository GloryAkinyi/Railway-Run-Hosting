
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('starter/',views.starter,name='starter'),
    path('about/',views.about,name='about'),
    path('appointment/',views.appointment,name='appointment'),
    path('show/',views.show,name='show'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),

    #Mpesa URLS

   #Mpesa URLS
    path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
