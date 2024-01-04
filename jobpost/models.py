from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from projectapp.models import User

# Create your models here.
class job_posts(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    company=models.CharField(max_length=200)
    poated_on=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=200)
    salary=models.IntegerField()
    type=models.CharField(max_length=200)
    experience=models.IntegerField()
    roles_and_responsibilities=models.TextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('details',kwargs={"pk":self.pk})
    
class submit(models.Model):
    # user=models.OneToOneField(job_posts,on_delete=models.CASCADE)
    jobtitle = models.ForeignKey(job_posts,related_name="job_posts",on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    emailid=models.EmailField()
    phone=models.IntegerField()

class addpost(models.Model):
    author_name=models.CharField(max_length=200)
    post_type=models.CharField(max_length=200)
    post_title=models.CharField(max_length=200)
    sub_title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="kiran",blank=True)
    time=models.DateTimeField(auto_now_add=True)
    view_count=models.IntegerField(blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='post_likes',default=None,blank=True)
    bookmarks=models.ManyToManyField(User,related_name='bookmarks',default=None,blank=True)

    def no_of_likes(self):
        return self.likes.count()

class comment(models.Model):
    Content = models.TextField()
    Date =models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    post = models.ForeignKey(addpost,related_name='add_posts', on_delete=models.CASCADE)
    # Author = models.ForeignKey(User,related_name='User',on_delete=models.CASCADE)
    Author = models.CharField(max_length=120)
    parent = models.ForeignKey('self',on_delete = models.CASCADE,blank = True,null=True,related_name='replies')

    def __str__(self):
        return self.Name
   
class subscribe(models.Model):
    Email=models.EmailField()
    Date=models.DateField(auto_now_add=True)