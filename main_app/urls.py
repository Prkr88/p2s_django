from django.urls import path

from main_app import views

#NameSpace:
app_name = 'main_app'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('order_parts/', views.order_parts, name='order_parts'),
    path('fleet_status/', views.fleet_status, name='fleet_status'),
    path('select_section/', views.select_section, name='select_section'),
    path('user_logout/', views.user_logout, name='user_logout'),
]