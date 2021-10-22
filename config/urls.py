"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from user_account.urls import urlpatterns as user_account_urls
from user_post.urls import urlpatterns as user_post_urls
from user_message.urls import urlpatterns as user_message_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += user_account_urls
urlpatterns += user_post_urls
urlpatterns += user_message_urls
