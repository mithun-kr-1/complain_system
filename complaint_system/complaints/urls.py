# complaints/urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('view_complaint/<int:complaint_id>/', views.view_complaint, name='view_complaint'),
    path('resolve_complaint/<int:complaint_id>/', views.resolve_complaint, name='resolve_complaint'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('track_complaint/', views.track_complaint, name='track_complaint'),
    path('officerlogin/', views.officerlogin, name='officerlogin')
    
]

