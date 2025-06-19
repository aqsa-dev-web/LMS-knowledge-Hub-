from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page

    # Current clean URLs
    path('teacher/login/', views.teacher_login, name='teacher_login'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('student/login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),

    path('logout/', views.logout_view, name='logout'),

    # Additional URLs to support .html endings (pointing to the same views)
    path('teacher-login.html', views.teacher_login, name='teacher_login_html'),
    path('teacher-dashboard.html', views.teacher_dashboard, name='teacher_dashboard_html'),

    path('student-login.html', views.student_login, name='student_login_html'),
    path('student-dashboard.html', views.student_dashboard, name='student_dashboard_html'),
]
