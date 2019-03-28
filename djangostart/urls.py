"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import django_cas_ng.views as cas_views
from django.contrib import admin
from django.urls import path
import message.views

urlpatterns = [
    # django 自带的后台管理
    path('admin/', admin.site.urls),

    path('index/', message.views.index, name="index"),
    path('protected/index/', message.views.protected, name='protected'),
    path('logout-j/', message.views.logout, name='logout'),
    path('form/', message.views.getform),

    # cas
    # 输入http://127.0.0.1:8089/accounts/login/跳转到 cas认证中心
    path('accounts/login/', cas_views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout/', cas_views.LogoutView.as_view(), name='cas_ng_logout'),
    path('accounts/callback/', cas_views.CallbackView.as_view(), name='cas_ng_proxy_callback'),

]
