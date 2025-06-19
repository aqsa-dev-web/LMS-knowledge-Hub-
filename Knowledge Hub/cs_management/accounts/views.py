from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'accounts/index.html')

def teacher_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'teacher' and password == '123456':  # Replace with real DB auth
            request.session['teacher_logged_in'] = True
            return redirect('teacher_dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'accounts/teacher-login.html')

def teacher_dashboard(request):
    if not request.session.get('teacher_logged_in'):
        return redirect('teacher_login')
    return render(request, 'accounts/teacher-dashboard.html')

def student_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'student' and password == '123456':  # Replace with real DB auth
            request.session['student_logged_in'] = True
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'accounts/student-login.html')

def student_dashboard(request):
    if not request.session.get('student_logged_in'):
        return redirect('student_login')
    return render(request, 'accounts/student-dashboard.html')

def logout_view(request):
    request.session.flush()
    return redirect('index')
