"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from tasks import views as task_views  # Import register view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Your app's views
    path('login/', task_views.login_view, name='login'),
    path('logout/', task_views.logout_view, name='logout'),
    path('register/', task_views.register_view, name='register'),
]