from django.shortcuts import render
from jobpost.models import job_posts,submit
from django.views.generic import DetailView
from jobpost.forms import submitform,addposts
# Create your views here.
def job(request):
    newjobs=job_posts.objects.all()
    # print(newjobs)
    return render(request,'sub/index.html',{'newjobs':newjobs})

class Jobdetails(DetailView):
    context_object_name='details'
    model=job_posts

def submits(request):
    register = False
    userform = submitform
    if request.method == 'POST':
        userform = submitform(request.POST)
        if userform.is_valid():
            userform.save()
            register = True
            print("hello")
    return render(request,"sub/submit.html",{'userform':userform,'register':register})

def appjobs(request):
    kiran=submit.objects.all()
    return render(request,"sub/appliedjobs.html",{"kiran":kiran})

def addpost(request):
    add=False
    form1=addposts()
    if request.method == 'POST':
        form1 = addposts(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            add = True
            print("hello")
    return render(request,"sub/add_post.html",{"form1":form1,'add':add})