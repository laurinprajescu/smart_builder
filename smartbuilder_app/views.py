# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import PostAJob
from .forms import JobPostForm
from accounts.models import User, TradesmanUser

from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, "home.html")

def how_it_works_page(request):
    return render(request, "howitworks.html")

def ineed_atradesman(request):
    return render(request, "ineedatradesman.html")

def iam_atradesman(request):
    return render(request, "iamatradesman.html")

def contact_page(request):
    return render(request, "contact.html")

def job_post_list(request):
    job_posts = PostAJob.objects.filter(published_date__lte=timezone.now()
              ).order_by('-published_date')
    return render(request, "postedjobs.html", {'job_posts': job_posts})

# def own_job_post(request):
#     if isinstance(request.user, User):
#         job_posts = PostAJob.objects.filter(author=request.user).order_by('-published_date')
#         return render(request, "ownpostedjobs.html", {'job_posts': job_posts})
#     else:
#         return render(request,"home.html")
  

# def own_job_post(request):
#     job_posts = PostAJob.objects.filter(author=request.user).order_by('-published_date')
#     return render(request, "ownpostedjobs.html", {'job_posts': job_posts})

# def is_tradesman(request, user):
#     try:
#         user.stripe_id
#         return True 
#     except:
#         return False

    

def new_job_post(request):
    if request.method == "POST":
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.author = request.user
            job_post.published_date = timezone.now()
            job_post.save()
            return render(request, "postedjobs.html")
    else:
        form = JobPostForm()
    return render(request, 'newjobpost.html', {'form': form})

def job_post_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    job_posts = get_object_or_404(PostAJob, pk=id)
    return render(request, "postedjobdetail.html", {'job_posts': job_posts})

@login_required
def edit_job_post(request, job_post_id):
   
   job_post = get_object_or_404(PostAJob, pk=job_post_id)
 
   if request.method == "POST":
       form = JobPostForm(request.POST, instance=job_post)
       if form.is_valid():
           form.save()
           messages.success(request, "You have updated your job!")
 
           return redirect(reverse('postedjobdetail'))
   else:
       form = JobPostForm(instance=job_post)
 
 
   args = {
       'form' : form,
       'form_action': reverse('edit_job_post',  kwargs={"job_post_id": job_post.id}),
       'button_text': 'Update Job'
   }
   args.update(csrf(request))
 
   return render(request, 'newjobpost.html', args)

@login_required
def delete_job_post(request, job_post_id):
   job_post = get_object_or_404(Post, pk=job_post_id)
   job_post.delete()
 
   messages.success(request, "Your job post was deleted!")
 
   return redirect(reverse('newjobpost', args={job_post_id}))