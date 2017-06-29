from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^team/([a-z0-9-]+)/$', views.team_member_detail, name = 'team_member_detail' ),
	url(r'^team/([a-z0-9-]+)/edit/', views.team_member_edit, name = 'team_member_edit' ),

]