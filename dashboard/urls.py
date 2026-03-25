from django.urls import path
from . import views
from .views import DashboardAPIView

urlpatterns = [
    path('', views.home, name='home'),  # HOME PAGE

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('api/data/', DashboardAPIView.as_view(), name='api_data'),
]