from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.load_mainpage),
    path('profile', views.load_profile),
    path('conspect_browse/', views.conspect_browse, name='conspect_browse'),
    path('login', views.load_login, name='login'),
    path('logout', views.log_out, name='logout'),
    path('register', views.load_signup),
    path('conspect', views.publish_conspect, name='conspect'),
    path('conspect_entries', views.conspect_entries, name='conspect_entries'),
    path('conspect_delete', views.conspect_delete, name='conspect_delete'),
    path('conspect_edit/<id>/', views.conspect_edit, name='conspect_edit'),
    path('tag/<tag>/', views.load_conspects_by_tag, name='tag'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate')
]
