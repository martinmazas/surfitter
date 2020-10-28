"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from surf_app import views
from boards import views as boardviews

urlpatterns = [
    path('', views.loginuser),
    path('admin/', admin.site.urls),
    # path('longboard/', views.longboard, name='longboard'),
    # path('customize/', views.customize, name='customize'),
    path('index/', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.createnewuser, name='createnewuser'),
    path('login/', views.loginuser, name='login'),
    path('newBoard/', boardviews.createNewBoard, name='createNewBoard'),
    path('longboard/', boardviews.boardload, name='loadlongboard'),
    path('customize/<str:pk>', boardviews.customize, name="customizePK"),
]