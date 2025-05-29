from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())
    
    context = {'forums':forums,
                'count':count,
                'discusisons':discussions}
    return render(request,'home.html',context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        forum = CreateInForum(request.POST)
        if form.is_valid():
            forum.save()
            return redirect('/')
        context = {'form':form}
        return render(request,'addInForum.html',context)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        forum = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'addInDiscussion.html',context)