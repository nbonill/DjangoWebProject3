"""
Definition of urls for DjangoWebProject3.
"""
from django.conf.urls import include, url
import DJ1.views
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls import include, url
import DJ1.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', DJ1.views.index, name='index'),
    url(r'^home$', DJ1.views.index, name='home'),
]


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', DJ1.views.index, name='index'),
    url(r'^home$', DJ1.views.index, name='home'),
]