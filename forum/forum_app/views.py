from django.shortcuts import render
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