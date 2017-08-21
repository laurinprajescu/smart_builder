from django.conf.urls import url
import views

urlpatterns = [
    url(r'^postedjobs/$', views.job_post_list),
    url(r'^newjobpost/$', views.new_job_post),
]