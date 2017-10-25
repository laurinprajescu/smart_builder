"""smart_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from smartbuilder_app import views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('smartbuilder_app.urls')),
    url(r'^$', views.home_page, name='home'),
    url(r'^howitworks/$', views.how_it_works_page, name='howitworks'),
    url(r'^ineedatradesman/$', views.ineed_atradesman, name='ineedatradesman'),
    url(r'^iamatradesman/$', views.iam_atradesman, name='iamatradesman'),
    url(r'^contact/$', views.contact_page, name='contact'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^tradesmanregister/$', accounts_views.tradesman_register, name='tradesmanregister'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
]