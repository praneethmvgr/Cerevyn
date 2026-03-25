from rest_framework.views import APIView
from rest_framework.response import Response
import random
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'User already exists'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')


class DashboardAPIView(APIView):
    """
    Returns realistic mock AI monitoring data:
    - Summary counts
    - Metrics with multiple datasets
    - Logs with timestamps
    """
    def get(self, request):
        statuses = ["Running", "Completed", "Failed"]
        logs = []
        running = completed = failed = 0
        metrics_running = []
        metrics_completed = []

        now = datetime.now()

        for i in range(10):
            status = random.choices(statuses, weights=[0.4, 0.4, 0.2])[0]

            if status == "Running":
                running += 1
            elif status == "Completed":
                completed += 1
            else:
                failed += 1

            log_time = now - timedelta(seconds=random.randint(0, 300))
            logs.append({
                "time": log_time.isoformat(),
                "status": status,
                "message": f"Task {i+1} {status}"
            })

            metrics_running.append(random.randint(10, 100))
            metrics_completed.append(random.randint(20, 120))

        return Response({
            "summary": {
                "totalTasks": len(logs),
                "runningTasks": running,
                "completedTasks": completed,
                "failedTasks": failed
            },
            "metrics": {
                "running": metrics_running,
                "completed": metrics_completed,
                "labels": [(now - timedelta(seconds=30*i)).strftime("%H:%M:%S") for i in reversed(range(10))]
            },
            "logs": sorted(logs, key=lambda x: x['time'], reverse=True)
        })
