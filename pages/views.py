from django.shortcuts import render, redirect



def homepage(request):
    return redirect('blog_list')