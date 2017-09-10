from django.conf.urls import url
import views

urlpatterns = [
    url(r'^postedjobs/$', views.job_post_list, name='postedjobs'),
    url(r'^newjobpost/$', views.new_job_post, name='newjobpost'),
    url(r'^postedjobs/(?P<id>\d+)/$', views.job_post_detail, name='postedjobdetail'),
    url(r'^newjobpost/edit/(?P<post_id>\d+)/$',views.edit_job_post, name='editjobpost'),
    url(r'^ownpostedjobs/$', views.own_job_post, name='ownpostedjobs'),
]