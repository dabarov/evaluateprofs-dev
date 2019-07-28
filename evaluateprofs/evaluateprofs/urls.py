"""evaluateprofs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from professors.views import (professors_list, professor_profile, home_page, 
                              about_page, terms_page)
from accounts.views import activate, login_view, logout_view, register_view


urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('professors/', professors_list),
    path('professors/<int:id>/', professor_profile),
    path('register/', register_view),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        activate, name='activate'),
    path('terms/', terms_page),
]
