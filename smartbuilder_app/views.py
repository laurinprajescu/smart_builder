# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import PostAJob
from .forms import JobPostForm

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
