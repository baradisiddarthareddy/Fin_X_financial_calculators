from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  # Set this route
    path('', views.signup_view),
    
    path('login/', auth_views.LoginView.as_view(template_name='calculators/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    path('rd/', views.rd_calculator, name='rd_calculator'),
    path('mis/', views.mis_calculator, name='mis_calculator'),
    path('gst/', views.gst_calculator, name='gst_calculator'),
    path('simple-interest/', views.simple_interest_calculator, name='simple_interest_calculator'),
    path('compound-interest/', views.compound_interest_calculator, name='compound_interest_calculator'),
    path('sukanya-calculator/', views.sukanya_calculator, name='sukanya_calculator'),
    path('sip-calculator/', views.sip_calculator, name='sip_calculator'),
    path('fd-calculator/', views.fd_calculator, name='fd_calculator'),
    path('loan-foreclosure/', views.loan_foreclosure_calculator, name='foreclosure_calculator'),
]

