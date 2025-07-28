from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('admin/ticket/<int:ticket_id>/', views.admin_ticket_detail, name='admin_ticket_detail'),
]
