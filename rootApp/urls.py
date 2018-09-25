from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.load_mainpage),
    path('profile', views.load_profile),
    path('login', views.load_login, name='login'),
    path('logout', views.log_out, name='logout'),
    path('register', views.load_signup),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate')
]
