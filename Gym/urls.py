"""Gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from management import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls')),
    url('^gymmembers/add/$', views.CreateGymMember.as_view(), name='add_gym_member'),
    url('^gymmembers/edit/(?P<_id>\d+)/$', views.UpdateGymMember.as_view(), name='edit_gym_member'),
    url('^setfeesstructure/$', views.set_fees_structure, name='set_fees_structure'),
    url('^removemember/$', views.remove_member, name='remove_member'),
    url('^payfees/$', views.pay_fees, name='pay_fees'),
    url('^gymmembers/$', views.list_gym_members, name='list_gym_members'),
    url('^checkfeesstatus/$', views.check_fees_status, name='check_fees_status'),
    url('^getmemberdetails/(?P<member_id>\d+)/$$', views.get_member_details, name='get_member_details'),
    url('^getmemberdetailsajax/$', views.get_member_details_ajax_call, name='get_member_details_ajax_call'),
    url('^markdailyattendance/$', views.mark_daily_attendance, name='mark_daily_attendance'),
    url('^$', views.home, name="home"),
    url('^generate_csv/$', views.generate_csv, name='generate_csv'),
    url('^generate_pdf/$', views.generate_pdf, name='generate_pdf'),
    url('^generic_view_gymmember/$', views.GymMemberList.as_view(), name='generic_view_gymmember')
]
