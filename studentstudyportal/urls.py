"""
URL configuration for studentstudyportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.conf import include
from dashboard import views as dashboard_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # urlpattern for "dashboard" app
    path("", include("dashboard.urls")),

    # urlpattern for "register" functionality
    path("register/", dashboard_views.register, name="register"),

    # urlpattern for "login" functionality
    path("login/", auth_views.LoginView.as_view(template_name = "dashboard/login.html"), name="login"),

    # url pattern for "profile" page
    path("profile/", dashboard_views.profile, name="profile"),

    # url pattern for "logout" functionality
    path("logout/", auth_views.LogoutView.as_view(template_name = "dashboard/logout.html"), name="logout"),
]