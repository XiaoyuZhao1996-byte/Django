from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'first_app'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('<int:question_id>/detail1/', views.detail1, name='detail1'),
    path('<int:question_id>/detail3/', views.detail3, name='detail3'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/question_status_modify/', views.question_status_modify, name='question_status_modify'),
    path('<int:choice_id>/question_modify_interval/', views.question_modify_interval, name='question_modify_interval'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
