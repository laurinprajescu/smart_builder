from django.conf.urls import url
import views

urlpatterns = [
    url(r'^postedjobs/$', views.job_post_list, name='postedjobs'),
    url(r'^newjobpost/$', views.new_job_post, name='newjobpost'),
    url(r'^postedjobs/(?P<id>\d+)/$', views.job_post_detail, name='postedjobdetail'),
    url(r'^ownpostedjobs/$', views.own_job_post, name='ownpostedjobs'),
    url(r'^postedjobs/(?P<job_post_id>\d+)/editjobpost/$', views.edit_job_post, name='editjobpost'),
    url(r'^postedjobs/(?P<job_post_id>\d+)/deletejobpost$', views.delete_job_post, name='deletejobpost'),
    url(r'^deletedjobpost/$', views.job_post_deleted, name='deletedjobpost'),
    url(r'^siteuserprofile/$', views.site_user_profile, name='siteuserprofile'),
    url(r'^email/$', views.email, name='email'),
    url(r'^success/$', views.success, name='success'),
    url(r'^choose/$', views.choose, name='choose'),
]