from django.urls import path
# from django.contrib.auth.decorators import login_required

from . import views

app_name = 'useremail'

urlpatterns = [

    path('subscribe/', views.subscribe, name='subscribe'),
]
