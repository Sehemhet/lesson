"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home import views

car_patterns = [
    path('<str:brand>/<str:model>/<int:year>', views.cardef),
    path('<str:brand>/<str:model>', views.cardef),
    path('<str:brand>', views.cardef),
    path('', views.cardef),
]

user_patterns = [
    path('<str:f_name>/<str:l_name>/<int:age>', views.user_info),
    path('<str:f_name>/<str:l_name>/', views.user_info),
    path('<str:f_name>/', views.user_info),
    path('', views.user_info),
]

urlpatterns = [
    path('car/', include(car_patterns)),
    path('admin/', admin.site.urls),
    path('', views.homedef, name='home'),
    path('person/', views.person),
    path('about/', views.about),
    path('info/', views.info),
    path('error/', views.error),
    path('index/', views.index),
    path('user/', include(user_patterns)),
]

