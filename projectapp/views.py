from django.shortcuts import render,get_object_or_404,redirect
from projectapp.forms import proj
from projectapp.models import User
from jobpost.models import addpost,comment,subscribe
from jobpost.forms import commentform,sub
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def index1(request):
    registered = False
    if request.method == 'POST':
        form = proj(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            print('username',form.cleaned_data['username'])
            registered = True

    else:
        form = proj()
    
    return render(request,"register.html",{'form':form ,'registered':registered})

def index2(request):
    if request.method == 'POST':
        print("hi")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            print("hello")
            if user.is_active:
                print("hellooooo")
                login(request,user)
                return redirect ("home")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("please check your cred.....!!")
    return render(request,"login.html",{})

@login_required(login_url="login")
def index3(request):
    form4=addpost.objects.all().order_by("-view_count")[0:3]  
    form5=addpost.objects.all().order_by("-view_count")[0:1]  
    frm=subscribe.objects.all()
    fm=sub()
    saved = False
    if request.method == 'POST':
        fm=sub(request.POST)
        if fm.is_valid():
            fm.save()
            saved = True
            print("Subscribe Successfully")
    return render(request,"home.html",{"form4":form4,'frm':frm,'fm':fm,'saved':saved,'form5':form5})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request,"dashboard.html",)

def blog(request):
    guru=addpost.objects.all()
    return render(request,"blog.html",{'guru':guru})

def jobdetails(request,pk):
    kiran=addpost.objects.get(pk=pk)
    cform = commentform()
    raj=addpost.objects.all()
    # likes code
    liked=False
    if kiran.likes.filter(id=request.user.id).exists():
        liked = True
    post_is_liked  = liked
    number_of_likes = kiran.no_of_likes()
    # book mark
    book=False
    if kiran.bookmarks.filter(id=request.user.id).exists():
        book = True
    book_is_click = book

    print("hi")
    if request.method == "POST":
        print('data comming')
        cform = commentform(request.POST)
        if cform.is_valid():
            parent_obj = None
            if request.POST.get('parent'):
                parent = request.POST.get('parent')
                parent_obj = comment.objects.get(id=parent)
                if parent_obj:
                    comment_reply = cform.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = kiran
                    comment_reply.save()
            else:
                print("valid success")
                print(request.POST.get('Name'))
                print(request.POST.get('Email'))
                comment1 = cform.save(commit=False)
                postid = request.POST.get('post_id')
                print("id->",postid)
                post = addpost.objects.get(id=postid)
                print("hi")
                comment1.post = post
                print('hi')
                comment1.save()
                print('hiiii')
    if kiran.view_count is None:
        kiran.view_count = 1
    else:
        kiran.view_count += 1
    kiran.save()

    k = comment.objects.filter(post=kiran)
    context = {'kiran':kiran, 'cform':cform ,'k':k,'raj':raj,'post_is_liked':post_is_liked,'number_of_likes':number_of_likes,'book_is_click':book_is_click}
    return render(request,"details.html",context)

def search(request):
    py = addpost.objects.all().order_by("-view_count")[0:3]  
    spider = addpost.objects.all().order_by("-time")[0:1]
    if request.method == 'POST':
        search_qry = request.POST['search_qry']
        posts = addpost.objects.filter(post_title__contains = search_qry)
        print(search_qry)
        return render(request,"search.html",{'search_qry':search_qry,'posts':posts,'py':py,'spider':spider})
    else:
     return render(request,"search.html",{'py':py,'spider':spider})
    
def like_post(request,pk):
    print(request.POST.get('post_id'))
    posts = get_object_or_404(addpost,id=request.POST.get('post_id'))
    print('x->',posts)


    if posts.likes.filter(id = request.user.id).exists():
        posts.likes.remove(request.user)
        print('removed')
    else:
        posts.likes.add(request.user)
        print("added")
    return redirect('jobdetails',pk=pk)


def bookmark(request,pk):
    post = get_object_or_404(addpost,id=request.POST.get('post_id'))
    print('x->',post)
    
    if post.bookmarks.filter(id = request.user.id).exists():
        post.bookmarks.remove(request.user)
        print('removed')
    else:
        post.bookmarks.add(request.user)
        print("added")
    return redirect('jobdetails',pk=pk)

def bookmarks(request):
    bk = addpost.objects.filter(bookmarks = request.user)
    print(bk)
    return render(request,'bookmark.html',{'bk':bk})


def liked(request):
    like = addpost.objects.filter(likes = request.user)
    print(like)
    return render(request,'liked.html',{'like':like})

   