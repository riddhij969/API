"""apiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiapp import views

# from apiapp.views import usersList, usersDetail, UserAuthentication
from apiapp.views import usersList, usersDetail

urlpatterns = [
    # path('admin/', admin.site.urls)
    # path('admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    # url(r'^api/users/', views.usersList.as_view())

    path('', usersList.as_view(), name= 'Home Page'),
    path('admin/', admin.site.urls),
    path('api/',views.Users.as_view()),
    url(r'^api/users/$', usersList.as_view(), name= 'users'),
    url(r'^api/users/(?P<first_name>\d+)/$',usersDetail.as_view(), name= 'users'),
    # url(r'^api/auth/$', UserAuthentication.as_view(), name= 'User Authentication API')

]
