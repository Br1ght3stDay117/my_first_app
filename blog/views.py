# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})
def index(request):
    return render(request,'blog/index.html',{})
def servicios(request):
    return render(request,'blog/services.html',{})
def contacto(request):
    return render(request,'blog/contact.html',{})
def galeria(request):
    return render(request,'blog/portfolio.html',{})
def iconos(request):
    return render(request,'blog/icons.html',{})
def tipografia(request):
    return render(request,'blog/typography.html',{})
def acerca_de(request):
    return render(request,'blog/about.html',{})